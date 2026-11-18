"""驗證資料結構及公開連結，輸出可下載的查核報告。"""
import argparse
from concurrent.futures import ThreadPoolExecutor
import csv
from datetime import datetime, timezone
from pathlib import Path
import re
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent

def check(url):
    try:
        with urlopen(Request(url, headers={"User-Agent": "TodolistTravelDataLinkCheck/1.0"}), timeout=18) as response:
            code, final = response.status, response.url
    except HTTPError as error:
        code, final = error.code, error.url
    except (URLError, TimeoutError, OSError):
        return "—", "—", "連線失敗，待複查"
    if code in (404, 410):
        return code, final, "失效"
    if code != 200:
        return code, final, "存取異常，待複查"
    return code, final, "正常" if final == url else "轉址，待核對"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--strict", action="store_true", help="有轉址或存取異常時回傳失敗")
    parser.add_argument("--output", type=Path, default=Path("link-health.md"))
    args = parser.parse_args()
    with (ROOT / "travel-data.csv").open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    required = {"分類", "站點", "方式", "出發前核對", "來源", "核對日期"}
    if not rows or any(set(row) != required or any(not value for value in row.values()) for row in rows):
        parser.error("資料欄位不完整")
    keys = {(row["分類"], row["站點"], row["方式"]) for row in rows}
    if len(keys) != len(rows):
        parser.error("交通資料有重複識別值")
    urls = {row["來源"] for row in rows}
    urls.update(re.findall(r"\]\((https://[^\s]+?)\)", (ROOT / "README.md").read_text()))
    accommodation = ROOT / "hotel-areas"
    if accommodation.is_dir():
        import json
        with (accommodation / "data.csv").open(encoding="utf-8", newline="") as stream:
            hotel_rows = list(csv.DictReader(stream))
        if not hotel_rows or hotel_rows != json.loads((accommodation / "data.json").read_text()):
            parser.error("住宿資料的 CSV 和 JSON 內容不同或無資料")
        hotel_keys = {(row["city"], row["area_or_station"]) for row in hotel_rows}
        if len(hotel_keys) != len(hotel_rows) or any(not value for row in hotel_rows for value in row.values()):
            parser.error("住宿資料有缺漏或重複列")
        urls.update(row["source_url"] for row in hotel_rows)
        urls.update(re.findall(r"\]\((https://[^\s]+?)\)", (accommodation / "README.md").read_text()))
    pages = ROOT / "docs" / "index.html"
    if pages.exists():
        from html import unescape
        urls.update(unescape(url) for url in re.findall(r'href="(https://[^"]+)"', pages.read_text()))
    if any(urlsplit(url).scheme != "https" or not urlsplit(url).hostname for url in urls):
        parser.error("來源必須為有效 HTTPS URL")
    print(f"資料列 {len(rows)}，外部 URL {len(urls)}")
    if args.offline:
        return
    urls = sorted(urls)
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(check, urls))
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    report = [f"# 連結健康檢查\n\n{date}\n", "| 原始 URL | HTTP | 最終 URL | 結果 |", "|---|---:|---|---|"]
    for url, (code, final, status) in zip(urls, results):
        report.append(f"| {url} | {code} | {final} | {status} |")
    args.output.write_text("\n".join(report) + "\n", encoding="utf-8")
    if args.strict and any(result[2] != "正常" for result in results):
        raise SystemExit(1)

if __name__ == "__main__":
    main()
