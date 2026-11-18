# Taiwan Hotel Near Stations Dataset｜台灣車站住宿區位

按隔日高鐵、臺鐵或市區捷運選住處。機捷站名、台鐵站名與飯店地址各自核對。

## 用法

在下面比較交通方式與出發前查核事項。也可下載 [CSV](data.csv) 或 [JSON](data.json)，依城市或下一程用途篩選。考慮輪椅、嬰兒車或大型行李時，先以營運方的電梯及無障礙路徑公告確認完整動線。

高鐵台中站在烏日，鄰近臺鐵新烏日站。若主要活動在臺中舊城，先比較住烏日與住市區的動線。

| 城市 | 站區 | 可核實銜接 | 適合先比較的情境 | 訂房前核對 | 來源 |
|---|---|---|---|---|---|
| 台北 | 機捷 A1 台北車站站區 | 機捷／臺鐵／高鐵／臺北捷運 | 跨運具接駁 | 核對住宿地址與地下街出口、最後一段步行動線。 | [來源](https://www.tymetro.com.tw/tymetro-new/tw/_pages/travel-guide/road.php) |
| 新北 | 板橋站區 | 台灣高鐵 | 新北住宿及長途鐵路 | 核對酒店靠板橋車站還是府中，分開安排步行與轉乘。 | [來源](https://www.thsrc.com.tw/) |
| 桃園 | A18 高鐵桃園站周邊 | 機捷／台灣高鐵 | 隔日機場或高鐵 | 確認出發航廈；住在站區仍需核對步行、接駁與末班。 | [來源](https://www.tymetro.com.tw/tymetro-new/tw/_pages/travel-guide/road.php) |
| 台中 | 烏日高鐵台中站周邊 | 高鐵／台鐵／捷運綠線 | 以高鐵和跨線轉乘為主 | 住宿靠高鐵入口或捷運入口會影響拖行李路線。 | [來源](https://www.thsrc.com.tw/ArticleContent/3301e395-46b8-47aa-aa37-139e15708779) |
| 台中 | 台中市區站周邊 | 台鐵台中站 | 市中心行程 | 利用臺鐵銜接新烏日，高鐵班次另查。 | [來源](https://www.thsrc.com.tw/ArticleContent/3301e395-46b8-47aa-aa37-139e15708779) |

## 資料字典

- `city`、`area_or_station` 為城市及比較單位，兩欄合併辨識一筆。
- `verified_connection` 為來源可核實的運輸連接或規劃參照。
- `planning_use_case` 及 `check_before_booking` 為 Todolist 編輯整理的選區情境與核對事項。
- `source_url` 與 `checked_on` 為該列的第一手來源及核對日期。

## 方法、限制與授權

逐列查營運機構或政府原始資料，整理基本站名及服務事實，另加原創的住宿選區判斷。涵蓋選定站區。班表、營運異動、無障礙狀態、酒店距離、價格與評價請向各營運方及酒店核對。原創文字及欄位設計依 [專案授權](../LICENSE.md) 提供，原始資料頁、地圖和商標各依權利人條款。

資料核對日期 2026-11-19。

## 延伸住宿攻略

- [台北住宿區域](https://todolist-taiwan.com/taipei-where-to-stay/)
- [板橋住宿區域](https://todolist-taiwan.com/banqiao-where-to-stay/)
- [台中住宿區域](https://todolist-taiwan.com/taichung-where-to-stay/)
