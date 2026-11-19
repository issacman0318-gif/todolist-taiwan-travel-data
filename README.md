# 臺北住宿位置與桃園機捷選站

以隔日交通選擇落腳站。A1 適合把臺鐵、高鐵與市區捷運列入比較，A3 可銜接環狀線，A18 適合直接接高鐵。板橋住宿另有其站區動線。

## 資料與工具

| 分類 | 站點 | 方式 | 出發前核對 |
|---|---|---|---|
| 臺北市區／臺鐵 | A1 台北車站 | 臺鐵、台灣高鐵、臺北捷運 | 各系統站區有步行距離，搭車前核對入口與出口。 |
| 新北環狀線 | A3 新北產業園區 | 新北捷運環狀線 | 核對行車方向與當日服務。 |
| 高鐵南下 | A18 高鐵桃園站 | 台灣高鐵 | 從 A12／A13 出發時查普通車停站，個別加班直達車須依公告。 |
| 搭機航廈 | A12 機場第一航廈 | 桃園機場 T1 | 先按航空公司及航班確認航廈。 |
| 搭機航廈 | A13 機場第二航廈 | 桃園機場 T2 | 回程查飯店附近車站至 T2 的時段。 |
| 住宿轉乘 | A1 台北車站站區 | 多線轉乘住宿區域 | 比對是否能從對應月台沿地下通道走到住宿附近。 |
| 住宿轉乘 | 板橋站區 | 高鐵與市區交通住宿區域 | 從機捷出發時另查轉乘路線及月台。 |

[下載 CSV](travel-data.csv)。欄位包括交通分類、站點、方式、行前查核事項、來源與核對日期。需要票價、班次或無障礙動線時，請在出發前查相應營運方。

使用 [線上桃園機捷選站器](https://issacman0318-gif.github.io/todolist-taiwan-travel-data/) 依下一段交通篩選，也可下載 [離線 HTML](docs/index.html) 後以瀏覽器開啟。

[桃園機場捷運轉乘圖卡（Pinterest）](https://www.pinterest.com/pin/710583647509591873/)整理 A1、A3 與 A18 三個轉乘選項，可以先用圖卡比較，再用選站器按行程篩選。

## 使用方式

執行 `python3 plan.py "高鐵南下"`，或省略條件列出全部。工具使用 Python 3 標準函式庫。

[開啟獨立住宿區位資料集](hotel-areas/README.md)，可下載 CSV／JSON 及查看逐列來源。

## 住宿與相關交通攻略

- [臺北住宿區域比較](https://todolist-taiwan.com/taipei-where-to-stay/)
- [板橋站周邊住宿選區](https://todolist-taiwan.com/banqiao-where-to-stay/)
- [桃園機場到台北交通](https://todolist-taiwan.com/taoyuan-airport-to-taipei/)
- [桃園機場到臺中的高鐵接駁](https://todolist-taiwan.com/taoyuan-airport-to-taichung/)

## 資料來源

- [來源 1](https://www.tymetro.com.tw/tymetro-new/tw/_pages/travel-guide/road.php)
- [來源 2](https://www.thsrc.com.tw/)

最近核對日期 2026-11-19。

## 官方網站

[Todolist Taiwan 官方網站](https://todolist-taiwan.com/)

## 授權與貢獻

[授權](LICENSE.md)涵蓋專案原創程式與文字。第三方來源維持各自的權利聲明。提交修正時請附官方資料 URL、查核日期及受影響的 CSV 列。可執行 `python3 check.py --offline` 先驗證資料結構。
