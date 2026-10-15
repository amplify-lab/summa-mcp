# 覆蓋率報告

由腳本從標準案例與規則清單產生，不手改。通過率是產生當下把每個案例真的丟給試算工具重跑的結果。

**官方案例**＝期望值來自官方試算工具、官方範例或條文裡的例題（`source_kind: official`）；**自行設計**＝期望值是我們依法源逐條算出（`derived`），算式對過法源但不是官方給的答案。兩種分開算，不合併成一個「通過率」。跟官方答案不一致的記在 [`DISCREPANCIES.md`](DISCREPANCIES.md)；法規與參數的變更紀錄在 [`CHANGELOG.md`](CHANGELOG.md)。

## 總表

| 項目 | 數量 |
|---|---|
| 試算工具（`calc_` 開頭） | 11 支 |
| 有標準案例的試算工具 | 11 支 |
| 規則 | 38 條 |
| 標準案例 | 104 個 |
| 官方案例 | 15 個（通過 15/15） |
| 自行設計案例 | 89 個（通過 89/89） |
| 可放對外範例（`public: true`） | 93 個 |
| 官方表格比對 | 2 張表、260 列（通過 260/260） |

## 每支試算工具

| 工具 | 規則 | 官方案例 | 自行設計案例 | 通過 | 說明 |
|---|---|---|---|---|---|
| `calc_annual_leave` | 2 | 0 | 6 | 6/6 |  |
| `calc_business_income_tax` | 1 | 0 | 5 | 5/5 |  |
| `calc_depreciation_tax_book_difference` | 1 | 0 | 3 | 3/3 |  |
| `calc_donation_limit` | 1 | 0 | 4 | 4/4 |  |
| `calc_entertainment_expense_limit` | 1 | 0 | 5 | 5/5 |  |
| `calc_labor_health_insurance` | 5 | 5 | 8 | 13/13 |  |
| `calc_overtime_pay` | 4 | 0 | 15 | 15/15 |  |
| `calc_personal_income_tax` | 9 | 0 | 11 | 11/11 |  |
| `calc_severance` | 4 | 0 | 8 | 8/8 |  |
| `calc_vat_payable` | 1 | 0 | 8 | 8/8 |  |
| `calc_withholding_and_nhi_supplement` | 9 | 10 | 16 | 26/26 |  |

## 每條規則

每條規則至少要有一般、邊界值、例外各一筆（標籤清單：一般、邊界值、例外）；缺的標籤列在「缺」欄。

| 規則 | 工具 | 官方 | 自行設計 | 通過 | 官方表格列 | 缺的標籤 | 已知不支援或待查 |
|---|---|---|---|---|---|---|---|
| `wht.professional_fee_resident`<br>居住者執行業務報酬：扣繳稅額（10%、2,000 元免扣）與二代健保補充保費（20,000 元起扣、2.11%） | `calc_withholding_and_nhi_supplement` | 0 | 3 | 3/3 | — | 例外 | 補充保費元以下的進位方式 |
| `wht.non_resident`<br>非居住者的各類所得扣繳（不適用 2,000 元免扣；稿費等七項 5,000 元以下免扣） | `calc_withholding_and_nhi_supplement` | 0 | 2 | 2/2 | — | 一般、邊界值 | 扣繳率欄位為待查的所得類別 |
| `nhi.bonus_over_4x`<br>所屬投保單位給付的獎金：全年累計逾投保金額 4 倍的部分計收補充保費 | `calc_withholding_and_nhi_supplement` | 5 | 1 | 6/6 | — | — | — |
| `nhi.part_time_salary`<br>非所屬投保單位給付的兼職薪資：達基本工資計收補充保費 | `calc_withholding_and_nhi_supplement` | 0 | 2 | 2/2 | — | 一般、例外 | — |
| `wht.salary_monthly`<br>居住者每月薪資扣繳：查扣繳稅額表，或未填免稅額申報表按 5% | `calc_withholding_and_nhi_supplement` | 0 | 5 | 5/5 | — | 例外 | 薪資起扣點尚未公告的年度；月薪超出稅額表列範圍的元以下處理 |
| `wht.salary_non_monthly`<br>非每月給付（獎金）與兼職所得扣繳：起扣標準以上按給付額 5% | `calc_withholding_and_nhi_supplement` | 0 | 3 | 3/3 | — | 例外 | 5% 扣繳稅額出現元以下尾數的進位 |
| `cit.rate`<br>營利事業所得稅：課稅所得 12 萬元以下免稅、超過部分的減半規則與稅率 | `calc_business_income_tax` | 0 | 5 | 5/5 | — | 例外 | — |
| `ent.limit`<br>交際費限額：進貨、銷貨、各業別累進比例，外銷收入與業別加計 | `calc_entertainment_expense_limit` | 0 | 5 | 5/5 | — | — | — |
| `don.limit`<br>營利事業捐贈列支限額：收益減損費後的比例；對政府捐贈不受限 | `calc_donation_limit` | 0 | 4 | 4/4 | — | — | — |
| `dep.straight_line`<br>固定資產折舊（平均法）的財稅差異：財務耐用年數與稅法耐用年數、殘值不同 | `calc_depreciation_tax_book_difference` | 0 | 3 | 3/3 | — | — | — |
| `vat.payable`<br>營業稅當期應納或溢付：銷項減進項、不得扣抵的進項、留抵 | `calc_vat_payable` | 0 | 8 | 8/8 | — | — | 只給整期銷售額時的銷項稅額進位；新設立營業人的第一期期間；電子發票小規模門檻 |
| `overtime.weekday`<br>平日延長工時加班費：前 2 小時 4/3、其後 5/3 | `calc_overtime_pay` | 0 | 5 | 5/5 | — | — | — |
| `overtime.rest_day`<br>休息日出勤：前 2 小時 4/3、第 3 至 8 小時 5/3、第 9 小時起 8/3；不足 4 小時以 4 小時計 | `calc_overtime_pay` | 0 | 5 | 5/5 | — | 例外 | — |
| `overtime.holiday`<br>國定假日出勤：8 小時內加給 1 日工資，延長工時照平日加給 | `calc_overtime_pay` | 0 | 4 | 4/4 | — | 邊界值、例外 | — |
| `overtime.regular_day_off_disaster`<br>例假因天災、事變、突發事件出勤：工資加倍並補假 | `calc_overtime_pay` | 0 | 1 | 1/1 | — | 一般、邊界值 | — |
| `ins.full_month`<br>整月投保：勞保、就保、職災、墊償基金、健保、勞退的勞工自付與雇主負擔（投保級距對應） | `calc_labor_health_insurance` | 0 | 3 | 3/3 | 28 | 例外 | — |
| `ins.prorate_days`<br>到職或退保當月按投保日數計（勞保、就保、職災按日；健保、勞退依規則） | `calc_labor_health_insurance` | 1 | 2 | 3/3 | — | 一般、邊界值 | — |
| `ins.part_time`<br>部分工時：勞保照最低級距投保 | `calc_labor_health_insurance` | 0 | 1 | 1/1 | — | 一般、邊界值 | — |
| `ins.health_dependents`<br>健保眷屬人數（本人加眷屬最多計 3 口）與雇主平均眷口數 | `calc_labor_health_insurance` | 3 | 1 | 4/4 | 232 | 例外 | 公民營事業受僱者以外的身分別（工會會員 60%、雇主 100%、公務人員 70%、私校教職員 35%、投保單位負擔 0%） |
| `ins.pension_voluntary`<br>勞退雇主提繳 6% 與勞工自願提繳 1%～6% | `calc_labor_health_insurance` | 1 | 1 | 2/2 | — | 邊界值、例外 | — |
| `leave.days`<br>特休日數（週年制）：滿 6 個月、1、2、3、5、10 年的日數 | `calc_annual_leave` | 0 | 5 | 5/5 | — | 例外 | — |
| `leave.unused_payout`<br>未休特休折發工資：日工資 × 未休日數 | `calc_annual_leave` | 0 | 1 | 1/1 | — | 邊界值、例外 | — |
| `sev.new_system`<br>新制資遣費：每滿 1 年給 1/2 個月平均工資、未滿 1 年比例計、最高 6 個月 | `calc_severance` | 0 | 4 | 4/4 | — | — | — |
| `sev.old_new_mixed`<br>新舊制並存：舊制每年 1 個月、未滿 1 個月以 1 個月計，新制每年 1/2 個月 | `calc_severance` | 0 | 1 | 1/1 | — | 一般、邊界值 | — |
| `sev.average_wage`<br>平均工資：最近 6 個月工資總額除以日數乘 30 | `calc_severance` | 0 | 1 | 1/1 | — | 邊界值、例外 | — |
| `sev.notice`<br>預告期與預告工資：3 個月以上 10 日、1 年以上 20 日、3 年以上 30 日 | `calc_severance` | 0 | 2 | 2/2 | — | 例外 | — |
| `pit.salary_only`<br>單身薪資所得：免稅額、標準扣除額、薪資特別扣除額與級距 | `calc_personal_income_tax` | 0 | 1 | 1/1 | — | 邊界值、例外 | — |
| `pit.household`<br>夫妻與受扶養親屬：三種計稅方式擇優（合併、薪資分開、各類分開） | `calc_personal_income_tax` | 0 | 2 | 2/2 | — | 邊界值、例外 | — |
| `pit.dividend`<br>股利：合併 8.5% 可抵減（上限 8 萬）或分開 28% | `calc_personal_income_tax` | 0 | 2 | 2/2 | — | 邊界值、例外 | — |
| `pit.basic_living_gap`<br>基本生活費差額（不含薪資特別扣除） | `calc_personal_income_tax` | 0 | 1 | 1/1 | — | 一般、邊界值 | — |
| `pit.rent_deduction`<br>房屋租金支出特別扣除額：實付金額與上限取低 | `calc_personal_income_tax` | 0 | 1 | 1/1 | — | 邊界值、例外 | — |
| `pit.wealth_exclusion`<br>高所得排富：薪資高於門檻不適用特定特別扣除 | `calc_personal_income_tax` | 0 | 1 | 1/1 | — | 一般、邊界值 | — |
| `pit.royalty_cost`<br>稿費：超過 18 萬的部分減除 30% 成本費用 | `calc_personal_income_tax` | 0 | 1 | 1/1 | — | 邊界值、例外 | — |
| `pit.amt`<br>基本稅額：海外所得計入基本所得額 | `calc_personal_income_tax` | 0 | 1 | 1/1 | — | 一般、邊界值 | — |
| `pit.year_not_announced`<br>年度公告還沒出時的處理（115 年度基本生活費、財產租賃費用標準） | `calc_personal_income_tax` | 0 | 1 | 1/1 | — | 一般、邊界值 | 115 年度基本生活費差額；115 年度財產租賃必要損耗及費用標準 |
| `nhi.interest`<br>利息所得的補充保費：單次給付達 20,000 元起扣、2.11%（不同存單分別判斷） | `calc_withholding_and_nhi_supplement` | 2 | 0 | 2/2 | — | 例外 | — |
| `nhi.rent`<br>租金收入的補充保費：單次給付達 20,000 元起扣、2.11%（一次付多個月以給付總額計） | `calc_withholding_and_nhi_supplement` | 2 | 0 | 2/2 | — | 例外 | — |
| `nhi.dividend`<br>股利所得的補充保費：單次給付達 20,000 元起扣、2.11% | `calc_withholding_and_nhi_supplement` | 1 | 0 | 1/1 | — | 邊界值、例外 | 雇主或自營業主身分投保者的股利：可扣除已列入投保金額計算的部分；臺灣存託憑證（TDR）股利（海外所得，不扣補充保費） |

## 官方表格比對

官方預先算好的金額表（或官方公布的整張表），每一列的輸入丟給試算工具，結果要跟表上金額一模一樣。這類比對一列就是一個官方答案，不用靠自己設計的算例。

| 表 | 規則 | 來源 | 查詢日 | 列數 | 通過 |
|---|---|---|---|---|---|
| 勞工保險保險費分擔金額表（勞保普通事故 11.5%＋就業保險 1%，115 年 1 月 1 日起）：28 級的勞工自付與單位負擔 | `ins.full_month` | [勞動部勞工保險局「勞工保險保險費分擔金額表」（政府資料開放平臺，JSON 下載 A17000000J-020015-t0a）](https://data.gov.tw/dataset/6259) | 2026-10-15 | 28 | 28/28 |
| 全民健康保險保險費負擔金額表（公、民營事業、機構及有一定雇主之受僱者，115 年 1 月 1 日起）：58 級 × 眷屬 0 至 3 人，本人（含眷屬）自付與投保單位負擔 | `ins.health_dependents` | [衛生福利部中央健康保險署「保險費負擔金額表（三）」](https://www.nhi.gov.tw/ch/cp-19418-9eefb-2576-1.html) | 2026-10-15 | 232 | 232/232 |

## 沒通過的案例

沒有。

## 已知不支援或待查的情境（每條規則）

### `wht.professional_fee_resident`
- **補充保費元以下的進位方式**：辦法與財政部說明都查不到（參數 nhi_supplement_rounding_rule 標待查）；工具一律四捨五入到元並在回應寫明

### `wht.non_resident`
- **扣繳率欄位為待查的所得類別**：代碼表該筆扣繳率待查時，工具回「待查，本試算不算」，不給猜的數字

### `wht.salary_monthly`
- **薪資起扣點尚未公告的年度**：資料沒有該年度的起扣點時，扣繳稅額不算（回明確原因，不套用上一年度）
- **月薪超出稅額表列範圍的元以下處理**：表外照表說明的公式算，元以下四捨五入的官方處理方式待查

### `wht.salary_non_monthly`
- **5% 扣繳稅額出現元以下尾數的進位**：辦法與財政部說明都查不到，待查（案例 wht_sal_08 的 4,525.05 不論四捨五入或捨去都是 4,525，不當硬性驗收）

### `vat.payable`
- **只給整期銷售額時的銷項稅額進位**：由銷售額估算銷項稅額，進位方式待查（工具回應寫明是估算）
- **新設立營業人的第一期期間**：參數 vat_new_business_first_period 標待查
- **電子發票小規模門檻**：參數 vat_einvoice_small_scale_threshold 標待查

### `ins.health_dependents`
- **公民營事業受僱者以外的身分別（工會會員 60%、雇主 100%、公務人員 70%、私校教職員 35%、投保單位負擔 0%）**：健保署公式頁有官方釋例；工具只算公民營事業有一定雇主的受僱者（本人 30%、單位 60%），沒有身分別輸入欄位

### `pit.year_not_announced`
- **115 年度基本生活費差額**：財政部尚未公告，工具回 null 並提醒（參數 pit_basic_living_expense 標待查）
- **115 年度財產租賃必要損耗及費用標準**：尚未公告，暫用 114 年度 43% 並提醒（參數 pit_rental_expense_rate 標待查）

### `nhi.dividend`
- **雇主或自營業主身分投保者的股利：可扣除已列入投保金額計算的部分**：官方實例（500 萬股利、全年投保金額 218 萬 4 千 → 59,418）；工具沒有對應的輸入欄位（讀碼推論），目前不支援
- **臺灣存託憑證（TDR）股利（海外所得，不扣補充保費）**：官方實例；工具沒有這個所得類別，目前不支援
