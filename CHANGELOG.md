# 法規與參數變更紀錄

由腳本從參數庫產生，不手改。依生效日由新到舊；每一列是同一項參數換新版：哪一天起、哪一項、舊值換成新值、依據哪一則公告或條文。法規全文的修正日在法規收錄清單（`list_laws`）。

共 38 筆換版，涵蓋 38 項參數。

| 生效日 | 參數 | 舊值 | 新值 | 依據 |
|---|---|---|---|---|
| 2026-01-01 | `amt_individual_deduction`<br>個人基本所得額扣除金額 | 7,500,000 TWD | 不變（新年度公告重新確認） | 所得基本稅額條例第 13 條第 1 項、第 3 項（金額依第 3 條第 2 項由財政部公告調整）；[公告115年度綜合所得稅及所得基本稅額相關免稅額、扣除額、課稅級距及計算退職所得定額免稅之金額（財政部新聞稿）](https://www.mof.gov.tw/singlehtml/384fb3077bb349ea973e7fc6f13b6974?cntId=34b463dc8f1b49f29d440d92a6fd5139) |
| 2026-01-01 | `amt_insurance_benefit_exempt`<br>受益人與要保人非同一人之保險死亡給付免計入基本所得額金額（每一申報戶全年合計） | 37,400,000 TWD | 不變（新年度公告重新確認） | 所得基本稅額條例第 12 條第 1 項第 2 款、第 5 項（金額由財政部公告調整）；[公告115年度綜合所得稅及所得基本稅額相關免稅額、扣除額、課稅級距及計算退職所得定額免稅之金額（財政部新聞稿）](https://www.mof.gov.tw/singlehtml/384fb3077bb349ea973e7fc6f13b6974?cntId=34b463dc8f1b49f29d440d92a6fd5139) |
| 2026-01-01 | `amt_overseas_income_threshold`<br>海外所得免計入基本所得額門檻（一申報戶全年合計未達） | 1,000,000 TWD | 不變（新年度公告重新確認） | 所得基本稅額條例第 12 條第 1 項第 1 款；[所得基本稅額條例第12條－全國法規資料庫](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=G0340115&flno=12) |
| 2026-01-01 | `amt_rate`<br>個人基本稅額稅率 | 0.2 | 不變（新年度公告重新確認） | 所得基本稅額條例第 13 條第 1 項；[所得基本稅額條例第13條－全國法規資料庫](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=G0340115&flno=13) |
| 2026-01-01 | `estate_brackets`<br>遺產稅課稅級距與累進差額 | （表格或多段，見參數庫） | 不變（新年度公告重新確認） | 遺產及贈與稅法第13條；第12條之1；財政部公告；[公告115年發生繼承或贈與案件適用遺產稅、贈與稅之免稅額、不計入遺產總額之金額、各項扣除額及課稅級距金額（財政部114年11月27日，台財稅字第11404671540號）](https://www.dot.gov.tw/singlehtml/ch26?cntId=266ef2de8dd54f9494bd5c399b3f323a) |
| 2026-01-01 | `estate_deductions`<br>遺產稅各項扣除額與不計入遺產總額金額 | （表格或多段，見參數庫） | 不變（新年度公告重新確認） | 遺產及贈與稅法第17條第1項第1款至第5款、第10款；第12條之1；財政部公告；[公告115年發生繼承或贈與案件適用遺產稅、贈與稅之免稅額、不計入遺產總額之金額、各項扣除額及課稅級距金額（財政部114年11月27日，台財稅字第11404671540號）](https://www.dot.gov.tw/singlehtml/ch26?cntId=266ef2de8dd54f9494bd5c399b3f323a) |
| 2026-01-01 | `estate_exemption`<br>遺產稅免稅額 | 13,330,000 TWD | 不變（新年度公告重新確認） | 遺產及贈與稅法第18條第1項；第12條之1；財政部公告；[公告115年發生繼承或贈與案件適用遺產稅、贈與稅之免稅額、不計入遺產總額之金額、各項扣除額及課稅級距金額（財政部114年11月27日，台財稅字第11404671540號）](https://www.dot.gov.tw/singlehtml/ch26?cntId=266ef2de8dd54f9494bd5c399b3f323a) |
| 2026-01-01 | `estate_military_exemption`<br>遺產稅軍警公教因執行職務死亡免稅額 | 26,660,000 TWD | 不變（新年度公告重新確認） | 遺產及贈與稅法第18條第1項後段；[遺產及贈與稅法第18條－全國法規資料庫](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=G0340072&flno=18) |
| 2026-01-01 | `gift_brackets`<br>贈與稅課稅級距與累進差額 | （表格或多段，見參數庫） | 不變（新年度公告重新確認） | 遺產及贈與稅法第19條第1項；第12條之1；財政部公告；[公告115年發生繼承或贈與案件適用遺產稅、贈與稅之免稅額、不計入遺產總額之金額、各項扣除額及課稅級距金額（財政部114年11月27日，台財稅字第11404671540號）](https://www.dot.gov.tw/singlehtml/ch26?cntId=266ef2de8dd54f9494bd5c399b3f323a) |
| 2026-01-01 | `gift_exemption`<br>贈與稅每年免稅額 | 2,440,000 TWD | 不變（新年度公告重新確認） | 遺產及贈與稅法第22條；第12條之1；財政部公告；[公告115年發生繼承或贈與案件適用遺產稅、贈與稅之免稅額、不計入遺產總額之金額、各項扣除額及課稅級距金額（財政部114年11月27日，台財稅字第11404671540號）](https://www.dot.gov.tw/singlehtml/ch26?cntId=266ef2de8dd54f9494bd5c399b3f323a) |
| 2026-01-01 | `min_wage_hourly`<br>每小時最低工資 | 190 TWD | 196 TWD | 最低工資法第 4、5 條（113-01-01 施行；第 18 條：其他法規關於基本工資之規定，適用最低工資）；勞動部公告；[最低工資連十漲！審議會決定自115年1月1日起，每月最低工資調升至29,500元，每小時最低工資調升至196元（勞動部）](https://www.mol.gov.tw/1607/1632/1633/84947/post) |
| 2026-01-01 | `min_wage_monthly`<br>每月最低工資 | 28,590 TWD | 29,500 TWD | 最低工資法第 4、5 條（113-01-01 施行；第 18 條：其他法規關於基本工資之規定，適用最低工資）；勞動部公告；[最低工資連十漲！審議會決定自115年1月1日起，每月最低工資調升至29,500元，每小時最低工資調升至196元（勞動部）](https://www.mol.gov.tw/1607/1632/1633/84947/post) |
| 2026-01-01 | `nhi_supplement_parttime_salary_exempt`<br>非所屬投保單位給付之薪資：單次給付未達此金額免扣補充保費（基本工資） | 28,590 TWD | 29,500 TWD | 全民健康保險扣取及繳納補充保險費辦法第 4 條第 2 項第 7 款；[全民健康保險扣取及繳納補充保險費辦法第 4 條](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=L0060027&flno=4) |
| 2026-01-01 | `pit_basic_living_expense`<br>每人基本生活所需費用 | 213,000 TWD | （無值） | 所得稅法第 17 條（基本生活費差額）；[公告115年度綜合所得稅及所得基本稅額相關免稅額、扣除額、課稅級距及計算退職所得定額免稅之金額（財政部）](https://www.mof.gov.tw/singlehtml/384fb3077bb349ea973e7fc6f13b6974?cntId=34b463dc8f1b49f29d440d92a6fd5139) |
| 2026-01-01 | `pit_brackets`<br>綜合所得稅課稅級距與稅率 | （表格或多段，見參數庫） | （表格或多段，見參數庫） | 所得稅法第 5 條第 2 項；[公告115年度綜合所得稅及所得基本稅額相關免稅額、扣除額、課稅級距及計算退職所得定額免稅之金額（財政部）](https://www.mof.gov.tw/singlehtml/384fb3077bb349ea973e7fc6f13b6974?cntId=34b463dc8f1b49f29d440d92a6fd5139) |
| 2026-01-01 | `pit_disability_special`<br>身心障礙特別扣除額（每人） | 218,000 TWD | 227,000 TWD | 所得稅法第 5 條、第 17 條（依財政部年度公告）；[公告115年度綜合所得稅及所得基本稅額相關免稅額、扣除額、課稅級距及計算退職所得定額免稅之金額（財政部）](https://www.mof.gov.tw/singlehtml/384fb3077bb349ea973e7fc6f13b6974?cntId=34b463dc8f1b49f29d440d92a6fd5139) |
| 2026-01-01 | `pit_dividend_credit_cap`<br>股利及盈餘可抵減稅額上限（每一申報戶每年） | 80,000 TWD | 不變（新年度公告重新確認） | 所得稅法第 15 條第 4 項；[所得稅法第15條－全國法規資料庫](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=G0340003&flno=15) |
| 2026-01-01 | `pit_dividend_credit_rate`<br>股利及盈餘可抵減稅額比率 | 0.085 | 不變（新年度公告重新確認） | 所得稅法第 15 條第 4 項；[所得稅法第15條－全國法規資料庫](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=G0340003&flno=15) |
| 2026-01-01 | `pit_dividend_separate_rate`<br>股利及盈餘分開計稅稅率 | 0.28 | 不變（新年度公告重新確認） | 所得稅法第 15 條第 5 項；[所得稅法第15條－全國法規資料庫](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=G0340003&flno=15) |
| 2026-01-01 | `pit_exemption`<br>免稅額（一般） | 97,000 TWD | 101,000 TWD | 所得稅法第 5 條、第 17 條（依財政部年度公告）；[公告115年度綜合所得稅及所得基本稅額相關免稅額、扣除額、課稅級距及計算退職所得定額免稅之金額（財政部）](https://www.mof.gov.tw/singlehtml/384fb3077bb349ea973e7fc6f13b6974?cntId=34b463dc8f1b49f29d440d92a6fd5139) |
| 2026-01-01 | `pit_exemption_70`<br>免稅額（年滿 70 歲之納稅義務人、配偶及直系尊親屬） | 145,500 TWD | 151,500 TWD | 所得稅法第 5 條、第 17 條（依財政部年度公告）；[公告115年度綜合所得稅及所得基本稅額相關免稅額、扣除額、課稅級距及計算退職所得定額免稅之金額（財政部）](https://www.mof.gov.tw/singlehtml/384fb3077bb349ea973e7fc6f13b6974?cntId=34b463dc8f1b49f29d440d92a6fd5139) |
| 2026-01-01 | `pit_itemized_donation_rate`<br>列舉扣除額：捐贈上限（占綜合所得總額比例） | 0.2 | 不變（新年度公告重新確認） | 所得稅法第 17 條第 1 項第 2 款第 2 目第 1 子目；[所得稅法第17條－全國法規資料庫](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=G0340003&flno=17) |
| 2026-01-01 | `pit_itemized_insurance_cap`<br>列舉扣除額：人身保險費每人每年上限 | 24,000 TWD | 不變（新年度公告重新確認） | 所得稅法第 17 條第 1 項第 2 款第 2 目第 2 子目；[所得稅法第17條－全國法規資料庫](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=G0340003&flno=17) |
| 2026-01-01 | `pit_itemized_mortgage_interest_cap`<br>列舉扣除額：自用住宅購屋借款利息每一申報戶每年上限 | 300,000 TWD | 不變（新年度公告重新確認） | 所得稅法第 17 條第 1 項第 2 款第 2 目第 5 子目；[所得稅法第17條－全國法規資料庫](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=G0340003&flno=17) |
| 2026-01-01 | `pit_long_term_care_special`<br>長期照顧特別扣除額（每人每年） | 180,000 TWD | 不變（新年度公告重新確認） | 所得稅法第 17 條；[所得稅法第 17 條](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=G0340003&flno=17) |
| 2026-01-01 | `pit_political_donation`<br>個人政治獻金列舉扣除（比例與每一申報戶上限） | （表格或多段，見參數庫） | 不變（新年度公告重新確認） | 政治獻金法第 19 條第 1 項；[政治獻金法第19條－全國法規資料庫](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=D0020049&flno=19) |
| 2026-01-01 | `pit_preschool_special`<br>幼兒學前特別扣除額 | （表格或多段，見參數庫） | 不變（新年度公告重新確認） | 所得稅法第 17 條；[所得稅法第 17 條](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=G0340003&flno=17) |
| 2026-01-01 | `pit_rent_special`<br>房屋租金支出特別扣除額（每申報戶每年上限） | 180,000 TWD | 不變（新年度公告重新確認） | 所得稅法第 17 條；[所得稅法第 17 條](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=G0340003&flno=17) |
| 2026-01-01 | `pit_rental_expense_rate`<br>出租房屋必要損耗及費用標準（一般房屋） | 0.43 | （無值） | 所得稅法第 14 條第 1 項第 5 類第 1 款；財政部每年公告「財產租賃必要損耗及費用標準」；[財政部主管法規共用系統：一百十二年度財產租賃必要損耗及費用標準（最近一份取得原文者）](https://law-out.mof.gov.tw/LawContent.aspx?id=GL011438) |
| 2026-01-01 | `pit_retirement_installment_exempt`<br>退職所得分期領取：全年減除金額 | 859,000 TWD | 894,000 TWD | 所得稅法第 14 條第 1 項第 9 類；[公告115年度綜合所得稅及所得基本稅額相關免稅額、扣除額、課稅級距及計算退職所得定額免稅之金額（財政部）](https://www.mof.gov.tw/singlehtml/384fb3077bb349ea973e7fc6f13b6974?cntId=34b463dc8f1b49f29d440d92a6fd5139) |
| 2026-01-01 | `pit_retirement_lump_exempt`<br>退職所得定額免稅：一次領取（每年服務年資） | （表格或多段，見參數庫） | （表格或多段，見參數庫） | 所得稅法第 14 條第 1 項第 9 類；[公告115年度綜合所得稅及所得基本稅額相關免稅額、扣除額、課稅級距及計算退職所得定額免稅之金額（財政部）](https://www.mof.gov.tw/singlehtml/384fb3077bb349ea973e7fc6f13b6974?cntId=34b463dc8f1b49f29d440d92a6fd5139) |
| 2026-01-01 | `pit_royalty_exempt`<br>稿費、版稅、樂譜、作曲、編劇、漫畫、講演鐘點費免稅額（每人每年） | 180,000 TWD | 不變（新年度公告重新確認） | 所得稅法第 4 條第 1 項第 23 款；[所得稅法第4條－全國法規資料庫](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=G0340003&flno=4) |
| 2026-01-01 | `pit_salary_expense_rate`<br>薪資所得核實減除必要費用上限（職業專用服裝費、進修訓練費、職業上工具支出，各占薪資收入比例） | 0.03 | 不變（新年度公告重新確認） | 所得稅法第 14 條第 1 項第 3 類第 1 款第 1、2、3 目；[所得稅法第14條－全國法規資料庫](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=G0340003&flno=14) |
| 2026-01-01 | `pit_salary_special`<br>薪資所得特別扣除額（每人） | 218,000 TWD | 227,000 TWD | 所得稅法第 5 條、第 17 條（依財政部年度公告）；[公告115年度綜合所得稅及所得基本稅額相關免稅額、扣除額、課稅級距及計算退職所得定額免稅之金額（財政部）](https://www.mof.gov.tw/singlehtml/384fb3077bb349ea973e7fc6f13b6974?cntId=34b463dc8f1b49f29d440d92a6fd5139) |
| 2026-01-01 | `pit_savings_invest_special`<br>儲蓄投資特別扣除額（全年上限） | 270,000 TWD | 不變（新年度公告重新確認） | 所得稅法第 17 條；[所得稅法第 17 條](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=G0340003&flno=17) |
| 2026-01-01 | `pit_std_married`<br>標準扣除額（有配偶） | 262,000 TWD | 272,000 TWD | 所得稅法第 5 條、第 17 條（依財政部年度公告）；[公告115年度綜合所得稅及所得基本稅額相關免稅額、扣除額、課稅級距及計算退職所得定額免稅之金額（財政部）](https://www.mof.gov.tw/singlehtml/384fb3077bb349ea973e7fc6f13b6974?cntId=34b463dc8f1b49f29d440d92a6fd5139) |
| 2026-01-01 | `pit_std_single`<br>標準扣除額（單身） | 131,000 TWD | 136,000 TWD | 所得稅法第 5 條、第 17 條（依財政部年度公告）；[公告115年度綜合所得稅及所得基本稅額相關免稅額、扣除額、課稅級距及計算退職所得定額免稅之金額（財政部）](https://www.mof.gov.tw/singlehtml/384fb3077bb349ea973e7fc6f13b6974?cntId=34b463dc8f1b49f29d440d92a6fd5139) |
| 2026-01-01 | `pit_tuition_special`<br>教育學費特別扣除額（每人每年上限） | 25,000 TWD | 不變（新年度公告重新確認） | 所得稅法第 17 條；[所得稅法第 17 條](https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=G0340003&flno=17) |

## 試算行為變更（不是參數換版）

| 日期 | 工具 | 變更 | 依據 |
|---|---|---|---|
| 2026-10-16 | `calc_business_income_tax` | 應納稅額的元以下由四捨五入改為無條件捨去，與財政部稅務入口網「營利事業所得稅試算」頁面一致；同一輸入最多差 1 元（例：課稅所得額 175,555 由 27,778 變 27,777；1,333,333 由 266,667 變 266,666；120,001 由 1 變 0）。回應的 `notices` 加一句說明。 | DISCREPANCIES DISC-005（維護者裁定）；官方試算頁 https://www.etax.nat.gov.tw/etwmain/etw158w/35（2026-10-16 實測）。元以下進位的法規明文查不到，找到明文再依明文 |

## 待查（沒有官方出處、不給值）

- `nhi_supplement_rounding_rule`：補充保險費扣取金額元以下四捨五入規則（全民健康保險扣取及繳納補充保險費辦法（未見元以下處理條文）；相關但適用對象待確認：全民健康保險法施行細則第 52 條第 1 項）
- `pit_basic_living_expense`：每人基本生活所需費用（所得稅法第 17 條（基本生活費差額））
- `pit_rental_expense_rate`：出租房屋必要損耗及費用標準（一般房屋）（所得稅法第 14 條第 1 項第 5 類第 1 款；財政部每年公告「財產租賃必要損耗及費用標準」）
- `vat_einvoice_small_scale_threshold`：小規模營業人使用統一發票之每月銷售額門檻（統一發票使用辦法第 4 條）
- `vat_new_business_first_period`：新設立營業人首期營業稅申報之期別規則（從哪一期起申報）（待查：營業稅法第 35 條、施行細則、稅籍登記規則均未見明文）
