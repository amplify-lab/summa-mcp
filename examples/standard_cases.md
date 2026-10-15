# 標準案例範例

93 個標準案例，全部是虛構數字。每個案例的輸入丟給對應的試算工具，結果要跟這裡的「結果」一模一樣（覆蓋率報告每次產生時重跑）。機器可讀的版本是 [`standard_cases.json`](standard_cases.json)。

「來源」欄：**官方**＝期望值來自官方試算工具、官方範例或條文例題；**自行設計**＝期望值是依法源逐條算出的算例。兩種分開計算。

## `calc_annual_leave`

| 編號 | 情境 | 輸入 | 結果 | 法源 | 來源 |
|---|---|---|---|---|---|
| leave_01 | 邊界：到職 2026-01-01、2026-07-01 滿 6 個月 → 3 日 | date 2026-10-03、hire_date 2026-01-01、as_of_date 2026-07-01 | result {"days":3} | 勞動基準法第 38 條 | 自行設計 |
| leave_02 | 邊界：到職 2024-10-02、2026-10-02 滿 2 年 → 10 日 | date 2026-10-03、hire_date 2024-10-02、as_of_date 2026-10-02 | result {"days":10} | 勞動基準法第 38 條 | 自行設計 |
| leave_03 | 邊界：到職 2021-10-02、2026-10-02 滿 5 年 → 15 日 | date 2026-10-03、hire_date 2021-10-02、as_of_date 2026-10-02 | result {"days":15} | 勞動基準法第 38 條 | 自行設計 |
| leave_04 | 邊界：到職 2016-10-02、2026-10-02 滿 10 年 → 16 日 | date 2026-10-03、hire_date 2016-10-02、as_of_date 2026-10-02 | result {"days":16} | 勞動基準法第 38 條 | 自行設計 |
| leave_05 | 一般：到職 2023-08-01、2026-10-02（3 年 2 個月）→ 14 日 | date 2026-10-03、hire_date 2023-08-01、as_of_date 2026-10-02 | result {"days":14} | 勞動基準法第 38 條 | 自行設計 |
| leave_06 | 一般：月薪 36,000、特休未休 4 日折發 4,800 | date 2026-10-03、hire_date 2020-01-01、as_of_date 2026-10-02、monthly_wage 36000、unused_days 4 | result {"unused_payout":4800} | 勞動基準法第 38 條 | 自行設計 |

## `calc_business_income_tax`

| 編號 | 情境 | 輸入 | 結果 | 法源 | 來源 |
|---|---|---|---|---|---|
| cit_01 | 免徵：課稅所得額 100,000 元 | taxable_income 100000 | tax_payable 0 | 所得稅法第 5 條第 5 項 | 自行設計 |
| cit_02 | 邊界：課稅所得額剛好 120,000 元 | taxable_income 120000 | tax_payable 0 | 所得稅法第 5 條第 5 項 | 自行設計 |
| cit_03 | 減半規則：課稅所得額 150,000 元 | taxable_income 150000 | tax_payable 15000 | 所得稅法第 5 條第 5 項 | 自行設計 |
| cit_04 | 邊界：課稅所得額 200,000 元（A、B 相等） | taxable_income 200000 | tax_payable 40000 | 所得稅法第 5 條第 5 項 | 自行設計 |
| cit_05 | 一般：課稅所得額 1,000,000 元 | taxable_income 1000000 | tax_payable 200000 | 所得稅法第 5 條第 5 項 | 自行設計 |

## `calc_depreciation_tax_book_difference`

| 編號 | 情境 | 輸入 | 結果 | 法源 | 來源 |
|---|---|---|---|---|---|
| dep_01 | 一般：整年取得，財務 3 年、稅法 5 年，無殘值 | cost 1200000、book_salvage 0、tax_salvage 0、book_life_years 3、tax_life_years 5、method straight_line、acquired_on 2026-01-01 | schedule [{"year":2026,"book_depreciation":400000,"tax_depreciation":240000,"difference":-160000,"cumulative_temporary_difference":-160000},{"year":2027,"book_depreciation":400000,"tax_depreciation":240000,"difference":-160000,"cumulative_temporary_difference":-320000},{"year":2028,"book_depreciation":400000,"tax_depreciation":240000,"difference":-160000,"cumulative_temporary_difference":-480000},{"year":2029,"book_depreciation":0,"tax_depreciation":240000,"difference":240000,"cumulative_temporary_difference":-240000},{"year":2030,"book_depreciation":0,"tax_depreciation":240000,"difference":240000,"cumulative_temporary_difference":0}] | 所得稅法第 51 條、第 54 條；營利事業所得稅查核準則第 95 條第 6 款、第 7 款 | 自行設計 |
| dep_02 | 邊界：7 月 1 日取得，取得當年與最後一年按月計，殘值 100,000 | cost 1000000、book_salvage 100000、tax_salvage 100000、book_life_years 4、tax_life_years 5、method straight_line、acquired_on 2026-07-01 | schedule [{"year":2026,"book_depreciation":112500,"tax_depreciation":90000,"difference":-22500,"cumulative_temporary_difference":-22500},{"year":2027,"book_depreciation":225000,"tax_depreciation":180000,"difference":-45000,"cumulative_temporary_difference":-67500},{"year":2028,"book_depreciation":225000,"tax_depreciation":180000,"difference":-45000,"cumulative_temporary_difference":-112500},{"year":2029,"book_depreciation":225000,"tax_depreciation":180000,"difference":-45000,"cumulative_temporary_difference":-157500},{"year":2030,"book_depreciation":112500,"tax_depreciation":180000,"difference":67500,"cumulative_temporary_difference":-90000},{"year":2031,"book_depreciation":0,"tax_depreciation":90000,"difference":90000,"cumulative_temporary_difference":0}] | 所得稅法第 51 條、第 54 條；營利事業所得稅查核準則第 95 條第 6 款、第 7 款 | 自行設計 |
| dep_03 | 例外：財稅殘值不同（財務預估殘值 50,000，稅上以無殘值計） | cost 500000、book_salvage 50000、tax_salvage 0、book_life_years 5、tax_life_years 5、method straight_line、acquired_on 2026-01-01 | schedule [{"year":2026,"book_depreciation":90000,"tax_depreciation":100000,"difference":10000,"cumulative_temporary_difference":10000},{"year":2027,"book_depreciation":90000,"tax_depreciation":100000,"difference":10000,"cumulative_temporary_difference":20000},{"year":2028,"book_depreciation":90000,"tax_depreciation":100000,"difference":10000,"cumulative_temporary_difference":30000},{"year":2029,"book_depreciation":90000,"tax_depreciation":100000,"difference":10000,"cumulative_temporary_difference":40000},{"year":2030,"book_depreciation":90000,"tax_depreciation":100000,"difference":10000,"cumulative_temporary_difference":50000}] | 所得稅法第 51 條、第 54 條；營利事業所得稅查核準則第 95 條第 6 款、第 7 款 | 自行設計 |

## `calc_donation_limit`

| 編號 | 情境 | 輸入 | 結果 | 法源 | 來源 |
|---|---|---|---|---|---|
| don_01 | 一般：受限捐贈 150,000 超過限額 | recognized_revenue 5000000、expenses_and_losses 3900000、donation_unlimited 500000、donation_capped 150000 | cap 100000、capped_allowed 100000、capped_disallowed 50000、unlimited_allowed 500000 | 所得稅法第 36 條；營利事業所得稅查核準則第 79 條第 1 款 | 自行設計 |
| don_02 | 邊界：受限捐贈剛好等於限額 | recognized_revenue 5000000、expenses_and_losses 3900000、donation_unlimited 0、donation_capped 100000 | cap 100000、capped_allowed 100000、capped_disallowed 0、unlimited_allowed 0 | 所得稅法第 36 條；營利事業所得稅查核準則第 79 條第 1 款 | 自行設計 |
| don_03 | 例外：損費已超過收益（X ≦ 0），受限捐贈限額為 0；對政府捐贈不受限 | recognized_revenue 2000000、expenses_and_losses 2500000、donation_unlimited 300000、donation_capped 80000 | cap 0、capped_allowed 0、capped_disallowed 80000、unlimited_allowed 300000 | 所得稅法第 36 條；營利事業所得稅查核準則第 79 條第 1 款 | 自行設計 |
| don_04 | 不受限：僅對各級政府捐贈 | recognized_revenue 3000000、expenses_and_losses 1000000、donation_unlimited 400000、donation_capped 0 | cap 181818、capped_allowed 0、capped_disallowed 0、unlimited_allowed 400000 | 所得稅法第 36 條；營利事業所得稅查核準則第 79 條第 1 款 | 自行設計 |

## `calc_entertainment_expense_limit`

| 編號 | 情境 | 輸入 | 結果 | 法源 | 來源 |
|---|---|---|---|---|---|
| ent_01 | 一般：一般申報，進貨 20,000,000、銷貨 30,000,000、實際交際費 200,000 | blue_form false、purchase_net 20000000、sales_net 30000000、freight_income_net 0、service_income_net 0、export_income 0、actual_expense 200000 | limit 165000、allowed 165000、disallowed 35000 | 營利事業所得稅查核準則第 80 條 | 自行設計 |
| ent_02 | 跨級：藍色申報書，進貨 200,000,000、銷貨 200,000,000 | blue_form true、purchase_net 200000000、sales_net 200000000、freight_income_net 0、service_income_net 0、export_income 0、actual_expense null | limit 1100000、allowed null、disallowed null | 營利事業所得稅查核準則第 80 條 | 自行設計 |
| ent_03 | 外銷加計：一般申報，進貨 60,000,000、銷貨 100,000,000、外銷收入 60,000,000 | blue_form false、purchase_net 60000000、sales_net 100000000、freight_income_net 0、service_income_net 0、export_income 60000000、actual_expense null | limit 1620000、allowed null、disallowed null | 營利事業所得稅查核準則第 80 條第 1 款第 7 目 | 自行設計 |
| ent_04 | 勞務業：一般申報，營業收益 50,000,000 | blue_form false、purchase_net 0、sales_net 0、freight_income_net 0、service_income_net 50000000、export_income 0、actual_expense null | limit 326000、allowed null、disallowed null | 營利事業所得稅查核準則第 80 條第 1 款第 4 目 | 自行設計 |
| ent_05 | 運輸客貨業：一般申報，運費收入 180,000,000 | blue_form false、purchase_net 0、sales_net 0、freight_income_net 180000000、service_income_net 0、export_income 0、actual_expense null | limit 900000、allowed null、disallowed null | 營利事業所得稅查核準則第 80 條第 1 款第 3 目 | 自行設計 |

## `calc_labor_health_insurance`

| 編號 | 情境 | 輸入 | 結果 | 法源 | 來源 |
|---|---|---|---|---|---|
| ins_01 | 一般：月投保薪資 36,300 整月 | date 2026-10-03、monthly_wage 36300 | labor_insurance {"employee_li_ei":908,"employer_li_ei":3176}、health_insurance {"employee":563,"employer":1757}、labor_pension {"employer":2178} | 勞工保險條例、就業保險法、勞工退休金條例、全民健康保險法；勞保局與健保署 115 年金額表 | 自行設計 |
| ins_02 | 邊界：月薪 29,500（最低級距），雇主勞保＋就保 2,582、墊償基金 7 | date 2026-10-03、monthly_wage 29500 | labor_insurance {"employer_li_ei":2582,"employer_wage_arrears_fund":7} | 勞工保險條例、就業保險法、勞工退休金條例、全民健康保險法；勞保局與健保署 115 年金額表 | 自行設計 |
| ins_03 | 例外：10/16 到職（當月按 15 日計），月投保 36,300 | date 2026-10-03、monthly_wage 36300、start_date 2026-10-16 | labor_insurance {"days":15,"employee_li_ei":453,"employer_li_ei":1588}、labor_pension {"employer":1089} | 勞工保險條例、就業保險法、勞工退休金條例、全民健康保險法；勞保局與健保署 115 年金額表 | 自行設計 |
| ins_04 | 例外：10/20 退保（當月按 20 日計），勞保投保薪資 40,100 | date 2026-10-03、labor_insured_salary 40100、end_date 2026-10-20 | labor_insurance {"days":20,"employee_li_ei":668,"employer_li_ei":2339} | 勞工保險條例、就業保險法、勞工退休金條例、全民健康保險法；勞保局與健保署 115 年金額表 | 自行設計 |
| ins_05 | 例外：部分工時月薪 8,000（勞保照最低級距 11,100） | date 2026-10-03、monthly_wage 8000、part_time true | labor_insurance {"insured_salary":11100,"employee_li_ei":277,"employer_li_ei":972} | 勞工保險條例、就業保險法、勞工退休金條例、全民健康保險法；勞保局與健保署 115 年金額表 | 自行設計 |
| ins_06 | 邊界：健保投保金額 40,100、眷屬 3 人（雇主負擔不看實際眷屬、用平均眷口數） | date 2026-10-03、nhi_insured_amount 40100、dependents 3 | health_insurance {"employee":2488,"employer":1940} | 勞工保險條例、就業保險法、勞工退休金條例、全民健康保險法；勞保局與健保署 115 年金額表 | 自行設計 |
| ins_07 | 邊界：月薪 31,000 對到投保級距 31,800（勞保、健保同級距） | date 2026-10-03、monthly_wage 31000 | labor_insurance {"insured_salary":31800,"employee_li_ei":795}、health_insurance {"employee":493} | 勞工保險條例、就業保險法、勞工退休金條例、全民健康保險法；勞保局與健保署 115 年金額表 | 自行設計 |
| ins_08 | 一般：勞退月提繳工資 45,800、自提 3% | date 2026-10-03、pension_wage 45800、voluntary_pension_rate 0.03 | labor_pension {"employee_voluntary":1374,"employer":2748} | 勞工保險條例、就業保險法、勞工退休金條例、全民健康保險法；勞保局與健保署 115 年金額表 | 自行設計 |
| nhi_off_11 | 一般：受僱者投保金額 53,000、眷屬 2 人，每月自付 2,466 | date 2026-10-03、nhi_insured_amount 53000、dependents 2 | health_insurance {"employee":2466} | 全民健康保險法第 18、27 條；健保署保險費計算公式（費率 5.17%、平均眷口數 0.56） | 官方 |
| nhi_off_12 | 一般：受僱者投保金額 53,000、無眷屬，每月自付 822 | date 2026-10-03、nhi_insured_amount 53000、dependents 0 | health_insurance {"employee":822} | 全民健康保險法第 18、27 條；健保署保險費計算公式（費率 5.17%、平均眷口數 0.56） | 官方 |
| nhi_off_13 | 一般：公民營事業有一定雇主受僱者投保金額 53,000，單位每月負擔 2,565 | date 2026-10-03、nhi_insured_amount 53000 | health_insurance {"employer":2565} | 全民健康保險法第 18、27 條；健保署保險費計算公式（費率 5.17%、平均眷口數 0.56） | 官方 |
| pen_off_01 | 一般：月提繳工資 36,300、雇主 6%、自願提繳 3.5%，全月：雇主 2,178、自提 1,271 | date 2026-10-03、pension_wage 36300、voluntary_pension_rate 0.035 | labor_pension {"employer":2178,"employee_voluntary":1271} | 勞工退休金條例第 14 條；勞保局退休金計算說明（每月以 30 日計、角以下四捨五入） | 官方 |
| pen_off_02 | 例外：2/25 到職（提繳 30−25+1＝6 天），月提繳工資 36,300、自願提繳 2.0%：雇主 436、自提 145 | date 2026-02-25、pension_wage 36300、voluntary_pension_rate 0.02、start_date 2026-02-25 | labor_pension {"employer":436,"employee_voluntary":145,"days":6} | 勞工退休金條例第 14 條；勞保局退休金計算說明（每月以 30 日計、角以下四捨五入） | 官方 |

## `calc_overtime_pay`

| 編號 | 情境 | 輸入 | 結果 | 法源 | 來源 |
|---|---|---|---|---|---|
| ot_01 | 一般：時薪 196，平日出勤 10 小時 | date 2026-10-03、pay_type hourly、wage 196、day_type weekday、hours_worked 10 | result {"total_for_the_day":2091} | 勞動基準法第 24 條、第 39 條、第 40 條；勞動部加班費試算器的算法（倍率用分數、無條件進位到元） | 自行設計 |
| ot_02 | 邊界：時薪 220，平日出勤 12 小時（日工時上限） | date 2026-10-03、pay_type hourly、wage 220、day_type weekday、hours_worked 12 | result {"total_for_the_day":3080} | 勞動基準法第 24 條、第 39 條、第 40 條；勞動部加班費試算器的算法（倍率用分數、無條件進位到元） | 自行設計 |
| ot_03 | 邊界：時薪 196，休息日 3 小時（元以下進位：849.33 → 850） | date 2026-10-03、pay_type hourly、wage 196、day_type rest_day、hours_worked 3 | result {"extra_pay":850} | 勞動基準法第 24 條、第 39 條、第 40 條；勞動部加班費試算器的算法（倍率用分數、無條件進位到元） | 自行設計 |
| ot_04 | 邊界：時薪 196，休息日 9 小時（第 9 小時起 8/3 倍） | date 2026-10-03、pay_type hourly、wage 196、day_type rest_day、hours_worked 9 | result {"extra_pay":3006} | 勞動基準法第 24 條、第 39 條、第 40 條；勞動部加班費試算器的算法（倍率用分數、無條件進位到元） | 自行設計 |
| ot_05 | 一般：時薪 210，休息日 11 小時 | date 2026-10-03、pay_type hourly、wage 210、day_type rest_day、hours_worked 11 | result {"extra_pay":4340} | 勞動基準法第 24 條、第 39 條、第 40 條；勞動部加班費試算器的算法（倍率用分數、無條件進位到元） | 自行設計 |
| ot_06 | 一般：時薪 196，國定假日 8 小時 | date 2026-10-03、pay_type hourly、wage 196、day_type holiday、hours_worked 8 | result {"total_for_the_day":3136} | 勞動基準法第 24 條、第 39 條、第 40 條；勞動部加班費試算器的算法（倍率用分數、無條件進位到元） | 自行設計 |
| ot_07 | 一般：時薪 196，國定假日 10 小時 | date 2026-10-03、pay_type hourly、wage 196、day_type holiday、hours_worked 10 | result {"total_for_the_day":3659} | 勞動基準法第 24 條、第 39 條、第 40 條；勞動部加班費試算器的算法（倍率用分數、無條件進位到元） | 自行設計 |
| ot_08 | 例外：時薪 196，例假因天災出勤 10 小時 | date 2026-10-03、pay_type hourly、wage 196、day_type regular_day_off_disaster、hours_worked 10 | result {"total_for_the_day":3920} | 勞動基準法第 24 條、第 39 條、第 40 條；勞動部加班費試算器的算法（倍率用分數、無條件進位到元） | 自行設計 |
| ot_09 | 邊界：日薪 1,600，休息日 8 小時 | date 2026-10-03、pay_type daily、wage 1600、day_type rest_day、hours_worked 8 | result {"extra_pay":2534} | 勞動基準法第 24 條、第 39 條、第 40 條；勞動部加班費試算器的算法（倍率用分數、無條件進位到元） | 自行設計 |
| ot_10 | 一般：月薪 42,000，平日出勤 9 小時（加班 1 小時） | date 2026-10-03、pay_type monthly、wage 42000、day_type weekday、hours_worked 9 | result {"extra_pay":234} | 勞動基準法第 24 條、第 39 條、第 40 條；勞動部加班費試算器的算法（倍率用分數、無條件進位到元） | 自行設計 |
| ot_11 | 一般：月薪 48,000，平日出勤 11 小時（加班 3 小時） | date 2026-10-03、pay_type monthly、wage 48000、day_type weekday、hours_worked 11 | result {"extra_pay":867} | 勞動基準法第 24 條、第 39 條、第 40 條；勞動部加班費試算器的算法（倍率用分數、無條件進位到元） | 自行設計 |
| ot_12 | 邊界：月薪 60,000，休息日 12 小時（日工時上限） | date 2026-10-03、pay_type monthly、wage 60000、day_type rest_day、hours_worked 12 | result {"extra_pay":5834} | 勞動基準法第 24 條、第 39 條、第 40 條；勞動部加班費試算器的算法（倍率用分數、無條件進位到元） | 自行設計 |
| ot_13 | 一般：月薪 36,000，國定假日 8 小時 | date 2026-10-03、pay_type monthly、wage 36000、day_type holiday、hours_worked 8 | result {"extra_pay":1200} | 勞動基準法第 24 條、第 39 條、第 40 條；勞動部加班費試算器的算法（倍率用分數、無條件進位到元） | 自行設計 |
| ot_14 | 一般：月薪 42,000，國定假日 10 小時 | date 2026-10-03、pay_type monthly、wage 42000、day_type holiday、hours_worked 10 | result {"extra_pay":1867} | 勞動基準法第 24 條、第 39 條、第 40 條；勞動部加班費試算器的算法（倍率用分數、無條件進位到元） | 自行設計 |
| ot_15 | 例外：月薪 32,000＋經常性津貼 3,400，平日出勤 11 小時（津貼計入時薪基數） | date 2026-10-03、pay_type monthly、wage 32000、monthly_regular_allowances 3400、day_type weekday、hours_worked 11 | result {"extra_pay":640} | 勞動基準法第 24 條、第 39 條、第 40 條；勞動部加班費試算器的算法（倍率用分數、無條件進位到元） | 自行設計 |

## `calc_severance`

| 編號 | 情境 | 輸入 | 結果 | 法源 | 來源 |
|---|---|---|---|---|---|
| sev_01 | 一般：新制年資 3 年 8 個月、平均工資 60,000 | date 2026-10-03、average_monthly_wage 60000、new_years 3、new_months 8 | result {"severance_total":110000} | 勞動基準法第 11、16、17 條；勞工退休金條例第 12 條；勞動部資遣費試算器的算法（資遣費無條件進位到元；預告工資四捨五入） | 自行設計 |
| sev_02 | 一般：新制年資 2 年 5 個月 12 日、平均工資 48,000 | date 2026-10-03、average_monthly_wage 48000、new_years 2、new_months 5、new_days 12 | result {"severance_total":58800} | 勞動基準法第 11、16、17 條；勞工退休金條例第 12 條；勞動部資遣費試算器的算法（資遣費無條件進位到元；預告工資四捨五入） | 自行設計 |
| sev_03 | 例外：新制年資 13 年、平均工資 70,000（上限 6 個月） | date 2026-10-03、average_monthly_wage 70000、new_years 13 | result {"severance_total":420000} | 勞動基準法第 11、16、17 條；勞工退休金條例第 12 條；勞動部資遣費試算器的算法（資遣費無條件進位到元；預告工資四捨五入） | 自行設計 |
| sev_04 | 邊界：新制年資 1 年 2 個月 20 日、平均工資 33,000（元以下無條件進位） | date 2026-10-03、average_monthly_wage 33000、new_years 1、new_months 2、new_days 20 | result {"severance_total":20167} | 勞動基準法第 11、16、17 條；勞工退休金條例第 12 條；勞動部資遣費試算器的算法（資遣費無條件進位到元；預告工資四捨五入） | 自行設計 |
| sev_05 | 例外：舊制 2002-03-01 起、2005-07-01 轉新制、2026-09-30 資遣，平均工資 62,000 | date 2026-10-03、average_monthly_wage 62000、old_system_start_date 2002-03-01、new_system_start_date 2005-07-01、end_date 2026-09-30 | result {"severance_total":578667} | 勞動基準法第 11、16、17 條；勞工退休金條例第 12 條；勞動部資遣費試算器的算法（資遣費無條件進位到元；預告工資四捨五入） | 自行設計 |
| sev_06 | 一般：用最近 6 個月工資 237,600、183 日算平均工資，新制年資 4 年 | date 2026-10-03、wages_last_6_months 237600、days_last_6_months 183、new_years 4 | result {"severance_total":77902} | 勞動基準法第 11、16、17 條；勞工退休金條例第 12 條；勞動部資遣費試算器的算法（資遣費無條件進位到元；預告工資四捨五入） | 自行設計 |
| sev_07 | 一般：年資 2 年、已預告 12 日、月薪 45,000 → 應預告 20 日、補 8 日、預告工資 12,000 | date 2026-10-03、service_months_for_notice 24、notice_days_given 12、monthly_wage_for_notice 45000 | result {"notice":{"required_days":20,"short_days":8,"notice_pay":12000}} | 勞動基準法第 11、16、17 條；勞工退休金條例第 12 條；勞動部資遣費試算器的算法（資遣費無條件進位到元；預告工資四捨五入） | 自行設計 |
| sev_08 | 邊界：年資 6 個月、未預告、月薪 29,500 → 預告 10 日、29,500÷30×10＝9,833.33 四捨五入 9,833 | date 2026-10-03、service_months_for_notice 6、notice_days_given 0、monthly_wage_for_notice 29500 | result {"notice":{"required_days":10,"short_days":10,"notice_pay":9833}} | 勞動基準法第 11、16、17 條；勞工退休金條例第 12 條；勞動部資遣費試算器的算法（資遣費無條件進位到元；預告工資四捨五入） | 自行設計 |

## `calc_vat_payable`

| 編號 | 情境 | 輸入 | 結果 | 法源 | 來源 |
|---|---|---|---|---|---|
| vat_01 | 一般：銷項大於進項 | output_tax 100000、input_tax 60000、non_deductible_input_tax 0、prior_credit 0、date 2026-09-30 | payable 40000、credit_carried 0 | 加值型及非加值型營業稅法第 15 條第 1 項、第 19 條、第 39 條第 2 項 | 自行設計 |
| vat_02 | 有不得扣抵的進項（交際應酬） | output_tax 100000、input_tax 70000、non_deductible_input_tax 3000、prior_credit 0、date 2026-09-30 | payable 33000、credit_carried 0 | 加值型及非加值型營業稅法第 15 條第 1 項、第 19 條、第 39 條第 2 項 | 自行設計 |
| vat_03 | 進項大於銷項：轉留抵 | output_tax 50000、input_tax 80000、non_deductible_input_tax 0、prior_credit 0、date 2026-09-30 | payable 0、credit_carried 30000 | 加值型及非加值型營業稅法第 15 條第 1 項、第 19 條、第 39 條第 2 項 | 自行設計 |
| vat_04 | 上期留抵抵完仍要繳 | output_tax 100000、input_tax 60000、non_deductible_input_tax 0、prior_credit 25000、date 2026-09-30 | payable 15000、credit_carried 0 | 加值型及非加值型營業稅法第 15 條第 1 項、第 19 條、第 39 條第 2 項 | 自行設計 |
| vat_05 | 上期留抵大於本期差額 | output_tax 100000、input_tax 60000、non_deductible_input_tax 0、prior_credit 50000、date 2026-09-30 | payable 0、credit_carried 10000 | 加值型及非加值型營業稅法第 15 條第 1 項、第 19 條、第 39 條第 2 項 | 自行設計 |
| vat_06 | 只給應稅銷售額：由稅率算銷項稅額 | taxable_sales 2000000、input_tax 42000、non_deductible_input_tax 0、prior_credit 0、date 2026-09-30 | payable 58000、credit_carried 0 | 加值型及非加值型營業稅法第 15 條第 1 項、第 19 條、第 39 條第 2 項 | 自行設計 |
| vat_07 | 剛好為 0 | output_tax 45000、input_tax 45000、non_deductible_input_tax 0、prior_credit 0、date 2026-09-30 | payable 0、credit_carried 0 | 加值型及非加值型營業稅法第 15 條第 1 項、第 19 條、第 39 條第 2 項 | 自行設計 |
| vat_08 | 三聯式與二聯式混合、含不得扣抵 | output_tax 125000、input_tax 70000、non_deductible_input_tax 3000、prior_credit 0、date 2026-09-30 | payable 58000、credit_carried 0 | 加值型及非加值型營業稅法第 15 條第 1 項、第 19 條、第 39 條第 2 項 | 自行設計 |

## `calc_withholding_and_nhi_supplement`

| 編號 | 情境 | 輸入 | 結果 | 法源 | 來源 |
|---|---|---|---|---|---|
| wht_nhi_01 | 一般：居住者執行業務報酬 50,000 元 | income_type_code 9A、amount 50000、residency resident、paid_by_insured_unit false、nhi_insured true | withholding_tax 5000、nhi_supplement 1055、net_paid 43945 | 各類所得扣繳率標準第 2、3、13 條；補充保險費辦法第 4 條 | 自行設計 |
| wht_nhi_02 | 邊界：居住者執行業務報酬 20,000 元（稅剛好 2,000 免扣；補充保費剛好達門檻） | income_type_code 9A、amount 20000、residency resident、paid_by_insured_unit false、nhi_insured true | withholding_tax 0、nhi_supplement 422、net_paid 19578 | 各類所得扣繳率標準第 2、3、13 條；補充保險費辦法第 4 條 | 自行設計 |
| wht_nhi_03 | 邊界：居住者執行業務報酬 19,999 元（稅免扣；補充保費未達門檻） | income_type_code 9A、amount 19999、residency resident、paid_by_insured_unit false、nhi_insured true | withholding_tax 0、nhi_supplement 0、net_paid 19999 | 各類所得扣繳率標準第 2、3、13 條；補充保險費辦法第 4 條 | 自行設計 |
| wht_nhi_04 | 例外：非居住者個人稿費 5,000 元（免扣）且未具健保資格 | income_type_code 9B、amount 5000、residency nonresident、paid_by_insured_unit false、nhi_insured false | withholding_tax 0、nhi_supplement 0、net_paid 5000 | 各類所得扣繳率標準第 3 條第 8 款；補充保險費辦法第 4 條第 2 項第 6 款 | 自行設計 |
| wht_nhi_05 | 例外：非居住者執行業務報酬 100,000 元（不適用 2,000 元免扣；未具健保資格） | income_type_code 9A、amount 100000、residency nonresident、paid_by_insured_unit false、nhi_insured false | withholding_tax 20000、nhi_supplement 0、net_paid 80000 | 各類所得扣繳率標準第 3 條第 8 款、第 13 條；補充保險費辦法第 4 條第 2 項第 6 款 | 自行設計 |
| wht_nhi_06 | 獎金：所屬投保單位給付，全年累計逾投保金額 4 倍的部分 | income_type_code 50、amount 100000、residency resident、paid_by_insured_unit true、salary_kind bonus、insured_amount 40000、bonus_cumulative_before 100000、nhi_insured true | withholding_tax 5000、nhi_supplement 844、net_paid 94156 | 全民健康保險法第 31 條第 1 項第 1 款；補充保險費辦法第 4 條第 1 項但書、第 6 條 | 自行設計 |
| wht_nhi_07 | 兼職薪資：非所屬投保單位給付 29,000 元（未達基本工資免扣補充保費） | income_type_code 50、amount 29000、residency resident、paid_by_insured_unit false、salary_kind other、nhi_insured true | withholding_tax 0、nhi_supplement 0、net_paid 29000 | 補充保險費辦法第 4 條第 2 項第 7 款 | 自行設計 |
| wht_nhi_08 | 兼職薪資：非所屬投保單位給付 30,000 元（達基本工資，計收補充保費） | income_type_code 50、amount 30000、residency resident、paid_by_insured_unit false、salary_kind other、nhi_insured true | withholding_tax 0、nhi_supplement 633、net_paid 29367 | 補充保險費辦法第 4 條第 1 項、第 2 項第 7 款 | 自行設計 |
| wht_sal_01 | 居住者每月薪資：查表，配偶及受扶養親屬 0 人，月薪 91,200 元 | income_type_code 50、amount 91200、residency resident、paid_by_insured_unit true、salary_kind other、nhi_insured true、salary_method table、dependents 0 | withholding_tax 2050、nhi_supplement 0、net_paid 89150 | 薪資所得扣繳辦法第 3、5、7 條第 1 項；115 年度薪資所得扣繳稅額表 | 自行設計 |
| wht_sal_02 | 居住者每月薪資：查表，0 人，月薪 90,501 元（表中最低的有稅額列） | income_type_code 50、amount 90501、residency resident、paid_by_insured_unit true、salary_kind other、nhi_insured true、salary_method table、dependents 0 | withholding_tax 2020、nhi_supplement 0、net_paid 88481 | 薪資所得扣繳辦法第 5、7 條第 1 項；115 年度薪資所得扣繳稅額表 | 自行設計 |
| wht_sal_03 | 居住者每月薪資：查表，0 人，月薪 100,000 元（表列 99,501 至 100,000） | income_type_code 50、amount 100000、residency resident、paid_by_insured_unit true、salary_kind other、nhi_insured true、salary_method table、dependents 0 | withholding_tax 2470、nhi_supplement 0、net_paid 97530 | 薪資所得扣繳辦法第 5 條；115 年度薪資所得扣繳稅額表說明（一）（二）（三）；115 年度綜合所得稅速算公式 | 自行設計 |
| wht_sal_04 | 居住者每月薪資：5% 定率（未填免稅額申報表），月薪 50,000 元 | income_type_code 50、amount 50000、residency resident、paid_by_insured_unit true、salary_kind other、nhi_insured true、salary_method flat | withholding_tax 2500、nhi_supplement 0、net_paid 47500 | 薪資所得扣繳辦法第 6 條第 1 項、第 7 條第 1 項；各類所得扣繳率標準第 2 條第 1 款第 2 目 | 自行設計 |
| wht_sal_05 | 居住者每月薪資：5% 定率，月薪 40,000 元（應扣稅額剛好 2,000，免扣） | income_type_code 50、amount 40000、residency resident、paid_by_insured_unit true、salary_kind other、nhi_insured true、salary_method flat | withholding_tax 0、nhi_supplement 0、net_paid 40000 | 薪資所得扣繳辦法第 6 條第 1 項、第 7 條第 1 項 | 自行設計 |
| wht_sal_06 | 居住者非每月給付：所屬投保單位發年終獎金 100,000 元（5% 加補充保費） | income_type_code 50、amount 100000、residency resident、paid_by_insured_unit true、salary_kind bonus、nhi_insured true、insured_amount 40000、bonus_cumulative_before 100000 | withholding_tax 5000、nhi_supplement 844、net_paid 94156 | 薪資所得扣繳辦法第 6 條第 2 項、第 7 條第 2 項第 1 款；補充保險費辦法第 4 條第 1 項但書、第 6 條 | 自行設計 |
| wht_sal_07 | 居住者兼職所得：非所屬投保單位給付 90,500 元（未達起扣標準，免扣稅） | income_type_code 50、amount 90500、residency resident、paid_by_insured_unit false、salary_kind other、nhi_insured false | withholding_tax 0、nhi_supplement 0、net_paid 90500 | 薪資所得扣繳辦法第 6 條第 2 項、第 7 條第 2 項第 1 款 | 自行設計 |
| wht_sal_08 | 居住者兼職所得：非所屬投保單位給付 90,501 元（剛達起扣標準，扣 5%） | income_type_code 50、amount 90501、residency resident、paid_by_insured_unit false、salary_kind other、nhi_insured false | withholding_tax 4525、nhi_supplement 0、net_paid 85976 | 薪資所得扣繳辦法第 6 條第 2 項、第 7 條第 2 項第 1 款 | 自行設計 |
| nhi_off_01 | 邊界：投保 31,800、年終獎金 100,000（未超過 4 倍 127,200）→ 補充保費 0 | residency resident、nhi_insured true、date 2021-08-05、income_type_code 50、amount 100000、paid_by_insured_unit true、salary_kind bonus、insured_amount 31800、bonus_cumulative_before 0 | result {"nhi_supplement":0} | 全民健康保險法第 31 條；全民健康保險扣取及繳納補充保險費辦法 | 官方 |
| nhi_off_02 | 一般：投保 31,800，已領 100,000 再領紅利 50,000（累計 150,000，超過 22,800）→ 481 | residency resident、nhi_insured true、date 2021-08-05、income_type_code 50、amount 50000、paid_by_insured_unit true、salary_kind bonus、insured_amount 31800、bonus_cumulative_before 100000 | result {"nhi_supplement":481} | 全民健康保險法第 31 條；全民健康保險扣取及繳納補充保險費辦法 | 官方 |
| nhi_off_03 | 一般：投保 38,200、一次領年終 180,000（超過 4 倍 27,200）→ 574 | residency resident、nhi_insured true、date 2021-08-05、income_type_code 50、amount 180000、paid_by_insured_unit true、salary_kind bonus、insured_amount 38200、bonus_cumulative_before 0 | result {"nhi_supplement":574} | 全民健康保險法第 31 條；全民健康保險扣取及繳納補充保險費辦法 | 官方 |
| nhi_off_04 | 例外：年中投保金額調為 40,100，累計 180,000 後再領 10,000（累計超過 29,600，取單次 10,000）→ 211 | residency resident、nhi_insured true、date 2021-08-05、income_type_code 50、amount 10000、paid_by_insured_unit true、salary_kind bonus、insured_amount 40100、bonus_cumulative_before 180000 | result {"nhi_supplement":211} | 全民健康保險法第 31 條；全民健康保險扣取及繳納補充保險費辦法 | 官方 |
| nhi_off_05 | 例外：同上，累計 190,000 後再領 5,000（累計超過 34,600，取單次 5,000）→ 106 | residency resident、nhi_insured true、date 2021-08-05、income_type_code 50、amount 5000、paid_by_insured_unit true、salary_kind bonus、insured_amount 40100、bonus_cumulative_before 190000 | result {"nhi_supplement":106} | 全民健康保險法第 31 條；全民健康保險扣取及繳納補充保險費辦法 | 官方 |
| nhi_off_06 | 一般：同一天到期三筆定存利息之一 25,000（單次達 20,000）→ 528 | residency resident、nhi_insured true、date 2021-08-05、income_type_code 5A、amount 25000、paid_by_insured_unit false | result {"nhi_supplement":528} | 全民健康保險法第 31 條；全民健康保險扣取及繳納補充保險費辦法 | 官方 |
| nhi_off_07 | 邊界：同一天到期三筆定存利息之一 3,500（單次未達 20,000）→ 不扣（0） | residency resident、nhi_insured true、date 2021-08-05、income_type_code 5A、amount 3500、paid_by_insured_unit false | result {"nhi_supplement":0} | 全民健康保險法第 31 條；全民健康保險扣取及繳納補充保險費辦法 | 官方 |
| nhi_off_08 | 一般：月租 100,000 一次付 6 個月租金 600,000 → 12,660 | residency resident、nhi_insured true、date 2021-08-05、income_type_code 51、amount 600000、paid_by_insured_unit false | result {"nhi_supplement":12660} | 全民健康保險法第 31 條；全民健康保險扣取及繳納補充保險費辦法 | 官方 |
| nhi_off_09 | 邊界：月租 20,000（剛好達單次門檻）→ 422，票面 19,578 | residency resident、nhi_insured true、date 2021-08-05、income_type_code 51、amount 20000、paid_by_insured_unit false | result {"nhi_supplement":422} | 全民健康保險法第 31 條；全民健康保險扣取及繳納補充保險費辦法 | 官方 |
| nhi_off_10 | 一般：股利 30,000 → 633 | residency resident、nhi_insured true、date 2021-08-05、income_type_code 54C、amount 30000、paid_by_insured_unit false | result {"nhi_supplement":633} | 全民健康保險法第 31 條；全民健康保險扣取及繳納補充保險費辦法 | 官方 |
