# 工具規格

由 `tools/gen-tool-spec.ts` 從工具定義產生，不手改。這份跟伺服器 `tools/list` 回傳的名稱、說明、輸入格式一致（伺服器網址 `https://mcp.summa.com.tw/mcp`）。所有工具都是唯讀：只查資料、只算數字，不寫入任何東西；伺服器只記匿名的使用統計，不記工具的參數值（見 README「我們記什麼、不記什麼」）。

共 25 支。每支回傳的結果都附官方出處（網址與標題）、生效日與查證日；試算另附每一步算式與用到的參數。遇到不支援或官方出處待查的情境，回明確的原因，不給猜的數字。

| 工具 | 用途 |
|---|---|
| [`bookkeeping_guide`](#bookkeeping_guide) | 記帳做法與常見判斷、函釋（每一題的第一步） |
| [`calc_annual_leave`](#calc_annual_leave) | 特休天數與未休折發試算 |
| [`calc_business_income_tax`](#calc_business_income_tax) | 營利事業所得稅試算 |
| [`calc_depreciation_tax_book_difference`](#calc_depreciation_tax_book_difference) | 平均法折舊的財稅差異試算 |
| [`calc_donation_limit`](#calc_donation_limit) | 營利事業捐贈限額試算 |
| [`calc_entertainment_expense_limit`](#calc_entertainment_expense_limit) | 交際費限額試算 |
| [`calc_labor_health_insurance`](#calc_labor_health_insurance) | 勞保、就保、職災、健保、勞退的勞工自付與雇主負擔試算 |
| [`calc_overtime_pay`](#calc_overtime_pay) | 加班費與休息日、國定假日、例假出勤的工資試算 |
| [`calc_personal_income_tax`](#calc_personal_income_tax) | 綜合所得稅試算（114、115 年度） |
| [`calc_severance`](#calc_severance) | 平均工資、資遣費、預告期與預告工資試算 |
| [`calc_vat_payable`](#calc_vat_payable) | 一期營業稅應納或留抵試算 |
| [`calc_withholding_and_nhi_supplement`](#calc_withholding_and_nhi_supplement) | 一筆給付的扣繳稅額、二代健保補充保費與實付金額試算 |
| [`filing_calendar`](#filing_calendar) | 某一年的申報與繳納期限（已套用假日順延） |
| [`foreign_per_diem`](#foreign_per_diem) | 國外出差生活費日支數額 |
| [`get_article`](#get_article) | 讀一條法規原文與修正日期 |
| [`get_data_version`](#get_data_version) | 資料版本與各類資料的查證日 |
| [`get_tax_parameter`](#get_tax_parameter) | 查某一天有效的稅率、級距、門檻、限額 |
| [`list_laws`](#list_laws) | 列出收錄的法規 |
| [`list_tax_parameters`](#list_tax_parameters) | 列出收錄的稅務參數 |
| [`lookup_code`](#lookup_code) | 代碼對照：扣繳所得類別、課稅別、會計項目、耐用年數、各縣市稅率等 |
| [`payroll_guide`](#payroll_guide) | 薪資、工時、加班、勞健保勞退、特休、資遣的做法（薪資題的第一步） |
| [`personal_tax_guide`](#personal_tax_guide) | 個人綜合所得稅做法（個人報稅題的第一步） |
| [`property_tax_guide`](#property_tax_guide) | 房地合一、土地增值稅、地價稅、房屋稅、契稅、遺產稅與贈與稅做法 |
| [`search_law`](#search_law) | 在法規全文裡用關鍵字找句子 |
| [`topic_map`](#topic_map) | 依問題類型列出該查哪幾部法規的哪幾條 |

## 試算工具的固定回傳欄位（0.3.0 起）

11 支 `calc_` 開頭的試算工具，回傳一律多三個欄位，位置與形狀固定（既有欄位照舊，沒有改名或換形狀）：

| 欄位 | 內容 |
|---|---|
| `rules` | 這次試算實際用到的規則：`[{ id, data_version, effective_from, coverage }]`。`id` 是 [COVERAGE.md](COVERAGE.md) 每條規則的編號；`effective_from` 是用到的參數裡最晚的生效日；`coverage` 是覆蓋率報告網址（不放通過率數字，數字會過期）。 |
| `source_refs` | 出處清單：`[{ title, url, verified_on }]`，由用到的參數彙整、以網址去重。（勞健保另有舊欄位 `sources`，是字串清單，維持原樣；`source_refs` 是新增的物件清單。） |
| `unsupported` | 工具沒算、或要人判斷的情況：`[{ code, message, legal_basis?, affects? }]`。沒有就是空陣列 `[]`，不會缺欄位。`affects` 是受影響的輸出欄位。 |

`unsupported.code`（公開後只增不改）：

| code | 什麼時候出現 |
|---|---|
| `retirement_conditions_met` | 舊制年資已符合退休條件（資遣費）：應給付退休金，不算資遣費 |
| `out_of_table_rounding` | 超出官方表列範圍，改用表說明的公式；元以下處理官方沒有明文 |
| `rate_pending` | 該所得類別的扣繳率官方出處待查，不給猜的數字 |
| `rounding_rule_pending` | 元以下進位方式官方沒有明文，工具四捨五入到元 |
| `year_not_announced` | 官方還沒公告該年度的數字：對應項目回 null，其餘照已公告的算（部分結果）。意思是「還沒有」 |
| `out_of_range` | 日期或數值超出工具收錄的範圍。大多數情況工具直接回錯誤 `out_of_range`、不回數字；這個代號只用在「仍回了結果、但其中某一項超出範圍沒算」。意思是「超出收錄」，與 `year_not_announced` 不同 |
| `subtotal_approximation` | 只給整期銷售額，銷項稅額是估算 |
| `input_missing` | 缺少某個輸入，結果中那一項沒算、其餘照算（例：沒帶行業別就不算職災保險費金額） |
| `category_not_supported` | 這個類別或情境工具不支援（兼營、非加值型、其他被保險人類別等） |
| `needs_judgement` | 要人判斷個案，工具不下結論 |

**`params_used` 預設精簡（0.4.0 起）**：試算回傳的 `params_used` 預設每個參數只有 `id`、`name`、`value`、`unit`、`effective_from`（狀態是「待查」的另有 `status`、`note`）；法源與出處網址在 `legal_basis`、`source_refs`，查證日在 `source_refs`。要每個參數的完整出處（`effective_to`、`legal_basis`、`source_url`、`source_title`、`verified_on`、`note`），在輸入帶 `detail: "full"`。`rules` 與 `source_refs` 不受影響。

**將淘汰的舊欄位**（0.3.0 先與新欄位並存，預計 0.4.0 起淘汰，屆時先在 CHANGELOG 公告）：`limitations`（`calc_withholding_and_nhi_supplement` 等 6 支，改看 `unsupported`）、`not_covered`（`calc_personal_income_tax`）、`warnings` 與 `notes` 中屬於「沒算」的部分、`source_url`（單一網址，改看 `source_refs`）、勞健保的 `sources`（字串清單，改看 `source_refs`）。

## 預設精簡的回應（0.5.0 起）

回應很大的幾支工具，預設回精簡版，要完整欄位在輸入帶 `detail: "full"`（`detail` 只有這一個值）：

| 工具 | 預設（精簡） | 完整（`detail: "full"`） |
|---|---|---|
| `list_tax_parameters`（不帶 `query` 時） | 每筆 `id`、`name`、`unit`、期數 | 每筆另有目前有效期間、法源、出處、查證日與各期 |
| `filing_calendar`（沒帶 `month` 時） | 每筆 `id`、`name`、`summary`、`due_date`、法源與適用對象；順延、延長、期間欄位有才回 | 每筆另有出處網址、查證日、順延依據、日曆來源 |
| `list_laws`（不帶 `category` 時） | 名稱、`pcode`、類別、修正日、條數 | 另有別名、查證日、官方連結與出處標題 |
| `bookkeeping_guide`、`payroll_guide`、`personal_tax_guide`、`property_tax_guide` | 找到相關段落就不回全部段落目錄（回 `toc_note`）；沒找到時照舊回目錄 | 輸入帶 `toc: true` 回全部段落目錄 |

`params_used` 的精簡見上一節（0.4.0）。


## bookkeeping_guide

台灣會計、記帳、稅務問題的第一步：先呼叫這支，帶題目的關鍵字（用題目原本的詞，好幾個小問都放進 query）。回相關的記帳做法、傳票與分錄範本、會計科目（商業會計項目表）、統一發票（開立時限、作廢、折讓）、營業稅與 401、進項扣抵、扣繳與二代健保入帳、暫估與沖回、預收預付、折舊、借款、股東往來、期末調整，附函釋字號與條號與每次都要照做的規則，並建議接著查哪支工具。回答前一定先查，不要憑記憶。薪資與勞健保先用 payroll_guide；稅率、期限、限額另用 get_tax_parameter、filing_calendar、calc_*。可用 section 指定目錄裡的段落。

**輸入**

| 欄位 | 型別 | 必填 | 說明 |
|---|---|---|---|
| `query` | string |  | 問題或關鍵字，例：「信用卡 年費 境外 沒有發票」「發票 折讓 已申報」「零用金 撥補」 |
| `section` | string |  | 指定段落的 id 或標題（目錄用 toc: true 取得） |
| `toc` | boolean |  | true＝回全部段落目錄（預設有找到段落就不回） |

## calc_annual_leave

算特休天數與未休折發金額。薪資題先呼叫 payroll_guide 再用這支。週年制：滿 6 個月 3 日、1 年 7 日、2 年 10 日、3 年 14 日、5 年 15 日、10 年起每年加 1 日到 30 日；部分工時按週工時比例；折發＝一日工資（月薪÷30）×未休日數。曆年制要另照勞動部特休試算器換算。另回 rules、source_refs、unsupported 三個固定欄位。

**輸入**

| 欄位 | 型別 | 必填 | 說明 |
|---|---|---|---|
| `hire_date` | string | 是 | YYYY-MM-DD；到職日 |
| `as_of_date` | string |  | YYYY-MM-DD；要算哪一天的特休（例：週年日）；沒帶用今天 |
| `part_time_weekly_hours` | integer |  | 部分工時每週工時（全時 40） |
| `unused_days` | number |  | 未休日數（算折發用） |
| `monthly_wage` | integer |  | 月薪（算一日工資＝月薪÷30） |
| `hourly_wage` | integer |  | 時薪（一日工資＝時薪×每日正常工時） |
| `daily_normal_hours` | integer |  | 時薪制每日正常工時（預設 8） |
| `detail` | string |  | full＝params_used 每個參數附完整出處與法源（預設精簡，出處看 source_refs）；可選值：full |

## calc_business_income_tax

試算營利事業所得稅（全年課稅所得額→應納稅額，含起徵額與超過部分減半），回每一步與用到的參數。不適用：未分配盈餘加徵、基本稅額、不滿 12 個月的營業年度；只是估算，不代替申報。另回 rules、source_refs、unsupported 三個固定欄位。

**輸入**

| 欄位 | 型別 | 必填 | 說明 |
|---|---|---|---|
| `taxable_income` | integer | 是 | 全年課稅所得額（元） |
| `date` | string |  | 有效日 YYYY-MM-DD，預設今天（台北） |
| `detail` | string |  | full＝params_used 每個參數附完整出處與法源（預設精簡，出處看 source_refs）；可選值：full |

## calc_depreciation_tax_book_difference

試算一項固定資產用平均法時，財務與稅上折舊的每年金額、差異與累計暫時性差異（取得當年與最後一年按月數比例）。不適用：定率遞減法等其他方法、耐用年數是否合規；只是估算，不代替申報。另回 rules、source_refs、unsupported 三個固定欄位。

**輸入**

| 欄位 | 型別 | 必填 | 說明 |
|---|---|---|---|
| `cost` | integer | 是 | 成本 |
| `book_salvage` | integer |  | 財務殘值 |
| `tax_salvage` | integer |  | 稅法預估殘值 |
| `book_life_years` | integer | 是 | 最小 1 |
| `tax_life_years` | integer | 是 | 最小 1 |
| `method` | string |  | 目前只有平均法；可選值：straight_line |
| `acquired_on` | string | 是 | 取得日 YYYY-MM-DD（取得月份整月計） |
| `date` | string |  | 有效日 YYYY-MM-DD，預設今天（台北） |
| `detail` | string |  | full＝params_used 每個參數附完整出處與法源（預設精簡，出處看 source_refs）；可選值：full |

## calc_donation_limit

試算營利事業捐贈限額：不受限的捐贈（如對政府）全數列支；對合格機關團體的捐贈限額 = X × 10% ÷ (1 + 10%)（X 是還沒減受限捐贈前的所得額，查核準則第 79 條），不是 X × 10%。輸入二選一：直接給 income_before_donation；或給 recognized_revenue 與 expenses_and_losses_excl_donations（損費不含任何捐贈）。不受限的捐贈帶 donation_unlimited，工具自己從所得額減掉，不要加進損費。不適用：政治獻金、文創、指定私校等其他限額；只是估算，不代替申報。另回 rules、source_refs、unsupported 三個固定欄位。

**輸入**

| 欄位 | 型別 | 必填 | 說明 |
|---|---|---|---|
| `income_before_donation` | integer |  | 未計任何捐贈前的所得額（收益減各項損費）；有這個就不用帶收益與損費 |
| `recognized_revenue` | integer |  | 經認定之收益總額 |
| `expenses_and_losses_excl_donations` | integer |  | 各項損費（不含任何捐贈） |
| `expenses_and_losses` | integer |  | 舊欄位（照舊義：各項損費含不受限的捐贈、不含受限的捐贈），請改用 expenses_and_losses_excl_donations |
| `donation_unlimited` | integer |  | 不受金額限制的捐贈 |
| `donation_capped` | integer |  | 受限額限制的捐贈 |
| `date` | string |  | 有效日 YYYY-MM-DD，預設今天（台北） |
| `detail` | string |  | full＝params_used 每個參數附完整出處與法源（預設精簡，出處看 source_refs）；可選值：full |

## calc_entertainment_expense_limit

試算交際費限額（進貨、銷貨、運費、勞務或信用業收入分級累進，加外銷特別交際費），一般申報與藍色申報書（含會計師簽證）比例不同。不適用：保險業、放映電影業；只是估算，不代替申報。另回 rules、source_refs、unsupported 三個固定欄位。

**輸入**

| 欄位 | 型別 | 必填 | 說明 |
|---|---|---|---|
| `blue_form` | boolean |  | 用藍色申報書或經會計師查核簽證申報，預設否 |
| `purchase_net` | integer |  | 全年進貨淨額 |
| `sales_net` | integer |  | 全年銷貨淨額 |
| `freight_income_net` | integer |  | 運輸客貨業全年運費收入淨額 |
| `service_income_net` | integer |  | 供給勞務或信用業全年營業收益淨額 |
| `export_income` | integer |  | 外銷收入 |
| `actual_expense` | integer |  | 實際交際費（選填，帶了才算允許列支與超限） |
| `date` | string |  | 有效日 YYYY-MM-DD，預設今天（台北） |
| `detail` | string |  | full＝params_used 每個參數附完整出處與法源（預設精簡，出處看 source_refs）；可選值：full |

## calc_labor_health_insurance

算勞保、就保、職災、墊償基金、健保、勞退的金額（勞工自付、雇主負擔）。薪資題先呼叫 payroll_guide 再用這支。照 115 年勞保局分擔金額表（勞保、就保各自算到元再相加，按投保日數）、健保署負擔金額表（眷屬最多 3 人、雇主按平均眷口數 0.56）、勞退月提繳分級表；部分工時有較低級距。到職、離職當月帶 start_date 或 end_date 按日計（每月 30 日；勞保、就保、職災、墊償基金退保算到退保是日，勞退月末日離職算整月 30 日，兩者在月底離職時日數可能不同；健保按月）。另回 rules、source_refs、unsupported 三個固定欄位。

**輸入**

| 欄位 | 型別 | 必填 | 說明 |
|---|---|---|---|
| `monthly_wage` | integer |  | 月薪資總額（含經常性給與）；用來對照勞保、健保、勞退的級距 |
| `labor_insured_salary` | integer |  | 直接指定勞保月投保薪資（要是分級表上的金額） |
| `occupational_insured_salary` | integer |  | 直接指定職災保險月投保薪資（要是《勞工職業災害保險投保薪資分級表》上的金額，29,500 到 72,800，跟勞保分級表是兩張表）；沒帶就用 monthly_wage 對職災分級表，再沒有才沿用勞保投保薪資 |
| `nhi_insured_amount` | integer |  | 直接指定健保投保金額 |
| `pension_wage` | integer |  | 直接指定勞退月提繳工資 |
| `part_time` | boolean |  | 是不是部分工時（薪資未達最低工資時勞保有較低級距） |
| `start_date` | string |  | YYYY-MM-DD；當月加保（到職）日；只算那一個月 |
| `end_date` | string |  | YYYY-MM-DD；當月退保（離職）日；勞保算到這一天（2月28日退保＝28日），勞退月末日離職算整月 30 日 |
| `dependents` | integer |  | 健保眷屬人數（最多計 3 人） |
| `industry_rate` | number |  | 職災保險行業別災害費率（例 0.0021 是 0.21%）；有帶才算職災保險費；跟 industry_code 都帶以這個為準 |
| `industry_code` | integer |  | 職災保險行業類別編號（1 到 55，勞動部公告表的編號；用 lookup_code kind=occupational_industry_rate 查）；帶了就用表列費率算職災保險費，date 在 2025-01-01 之前回 not_found |
| `voluntary_pension_rate` | number |  | 勞工自願提繳率（0 到 0.06） |
| `date` | string |  | YYYY-MM-DD；用哪一天有效的表；沒帶用 start_date、end_date 或今天 |
| `detail` | string |  | full＝params_used 每個參數附完整出處與法源（預設精簡，出處看 source_refs）；可選值：full |

## calc_overtime_pay

算加班費、休息日、國定假日、例假出勤的工資。薪資題先呼叫 payroll_guide 再用這支；好幾天或好幾段的，每一段各呼叫一次再加總。照勞動部加班費試算器：月薪÷30÷8 求每小時工資額；平日延長 4/3、5/3；休息日 4/3、5/3、8/3（按實際時數）；國定假日月薪制 8 小時內加發一日工資、時薪制按時數加倍；例假（天災）加倍並補假；無條件進位到元。回每一段的倍率、算式、合計與違法提醒。另回 rules、source_refs、unsupported 三個固定欄位。

**輸入**

| 欄位 | 型別 | 必填 | 說明 |
|---|---|---|---|
| `pay_type` | string | 是 | 計薪方式：時薪、日薪、月薪；可選值：hourly、daily、monthly |
| `wage` | integer | 是 | 時薪、日薪或月薪（元） |
| `monthly_regular_allowances` | integer |  | 月薪制：每月固定發的經常性給與（伙食津貼、全勤獎金、職務加給等）合計，會加進月薪算每小時工資額 |
| `daily_normal_hours` | integer |  | 日薪制：約定每日正常工時（預設 8） |
| `day_type` | string | 是 | 那一天：平日、休息日、國定假日或特休日、例假（因天災、事變、突發事件出勤）；可選值：weekday、rest_day、holiday、regular_day_off_disaster |
| `hours_worked` | number | 是 | 那一天實際工作時數（不含休息；可用小數，例 9.5） |
| `disaster` | boolean |  | 平日或休息日是不是因天災、事變、突發事件延長工時 |
| `date` | string |  | YYYY-MM-DD；用哪一天有效的最低工資；沒帶用今天 |
| `detail` | string |  | full＝params_used 每個參數附完整出處與法源（預設精簡，出處看 source_refs）；可選值：full |

## calc_personal_income_tax

算個人綜所稅的應納稅額、應補或應退。第一步先呼叫 personal_tax_guide 讀做法，再用這支。照所得年度的財政部公告（114、115 年度）：各類所得、免稅額（70 歲、115 年度起未成年子女加 50%）、標準或列舉取高、特別扣除額與排富、基本生活費差額（比較項目不含薪資特扣）、級距與累進差額；有配偶的把全部合併、薪資分開、各類所得分開都算，有股利的再比 8.5% 可抵減與 28% 分開，回每一種的結果與最低的那一種、每一步算式與參數出處。只是試算，不代替申報。另回 rules、source_refs、unsupported 三個固定欄位。

**輸入**

| 欄位 | 型別 | 必填 | 說明 |
|---|---|---|---|
| `income_year` | integer | 是 | 所得年度（西元或民國都可以）：114 年度＝2025 年所得、2026 年 5 月申報，帶 2025 或 114 |
| `members` | 陣列（object） | 是 | 申報戶每個人一筆；本人一定要有 |
| `household` | object |  |  |
| `method` | string |  | 只看某一種計稅方式（選填，名稱照 options 的 method） |
| `detail` | string |  | full＝params_used 每個參數附完整出處與法源（預設精簡，出處看 source_refs）；可選值：full |

## calc_severance

算資遣費、平均工資、預告期與預告工資。薪資題先呼叫 payroll_guide 再用這支。照勞動部資遣費試算器：新制基數 (360×年＋30×月＋日)÷720、最高 6 個月；舊制每滿 1 年 1 個月、未滿以 1 個月計、無上限；資遣費無條件進位到元，預告工資四捨五入到元。預告期：3 個月以上 1 年未滿 10 日、1 年以上 3 年未滿 20 日、3 年以上 30 日。有舊制年資且全部工作年資滿 25 年：舊制部分已符合退休條件，應給付退休金不是資遣費，不算（`result.old_system.status` 是 `retirement_conditions_met`、`severance_total` 是 null、回 unsupported；新制照算在 `new_system_only_total`）；滿 10 年只在 notes 提示（年齡條件工具不判斷）。另回 rules、source_refs、unsupported 三個固定欄位。

**輸入**

| 欄位 | 型別 | 必填 | 說明 |
|---|---|---|---|
| `average_monthly_wage` | integer |  | 平均工資（月）；沒有就帶前 6 個月工資總額與日數 |
| `wages_last_6_months` | integer |  | 事由發生前 6 個月工資總額（含加班費、經常性獎金） |
| `days_last_6_months` | integer |  | 那 6 個月的總日數（例 183） |
| `new_system_start_date` | string |  | YYYY-MM-DD；新制年資起日（例 2005-07-01 或到職日） |
| `old_system_start_date` | string |  | YYYY-MM-DD；舊制年資起日（94 年 7 月 1 日前到職、保留舊制年資的） |
| `end_date` | string |  | YYYY-MM-DD；契約終止日 |
| `new_years` | integer |  | 新制年資：年 |
| `new_months` | integer |  | 新制年資：月 |
| `new_days` | integer |  | 新制年資：日 |
| `old_years` | integer |  | 舊制年資：年 |
| `old_months` | integer |  | 舊制年資：月 |
| `old_days` | integer |  | 舊制年資：日 |
| `service_months_for_notice` | integer |  | 算預告期用的繼續工作月數（沒帶就用年資） |
| `notice_days_given` | integer |  | 已經預告的日數 |
| `monthly_wage_for_notice` | integer |  | 算預告工資用的月薪（一日工資＝月薪÷30；平均工資每日較高的以平均工資計，勞動部 109.10.29 令釋） |
| `date` | string |  | YYYY-MM-DD；用哪一天有效的規則 |
| `detail` | string |  | full＝params_used 每個參數附完整出處與法源（預設精簡，出處看 source_refs）；可選值：full |

## calc_vat_payable

試算一期營業稅：銷項稅額減可扣抵進項稅額，再用上期累積留抵抵減，回本期應納與留抵下期，附每步算式與參數。不適用：兼營應稅與免稅的比例扣抵、外銷零稅率與固定資產退稅、特種稅額、小規模營業人查定；只帶銷售額時以整期銷售額估算；只是估算，不代替申報。另回 rules、source_refs、unsupported 三個固定欄位。

**輸入**

| 欄位 | 型別 | 必填 | 說明 |
|---|---|---|---|
| `output_tax` | integer |  | 本期銷項稅額（已扣銷貨退回與折讓）；跟 taxable_sales 二選一 |
| `taxable_sales` | integer |  | 本期應稅銷售額（沒帶 output_tax 時照一般稅率估算） |
| `input_tax` | integer | 是 | 本期進項稅額合計 |
| `non_deductible_input_tax` | integer |  | 其中不得扣抵的進項稅額（營業稅法第 19 條） |
| `prior_credit` | integer |  | 上期累積留抵稅額 |
| `date` | string |  | 有效日 YYYY-MM-DD，預設今天（台北） |
| `detail` | string |  | full＝params_used 每個參數附完整出處與法源（預設精簡，出處看 source_refs）；可選值：full |

## calc_withholding_and_nhi_supplement

試算一筆給付的扣繳稅額、二代健保補充保費與實付金額，回每一步算式與用到的參數。員工薪資、獎金、兼職、工讀生先呼叫 payroll_guide 讀做法。適用：執行業務、租賃、利息、權利金、獎金等照扣繳率標準扣繳的所得。居住者薪資要帶 paid_by_insured_unit 與 salary_kind：每月薪資照 salary_method（table 查薪資扣繳稅額表、flat 按全月 5%），獎金與兼職按每次給付 5%。不適用：按日給付的臨時工、津貼與補助款、租稅協定、個案核定；函釋與個案判斷不在這裡；只是估算，不代替申報。另回 rules、source_refs、unsupported 三個固定欄位。

**輸入**

| 欄位 | 型別 | 必填 | 說明 |
|---|---|---|---|
| `income_type_code` | string | 是 | 所得類別代號（例 9A、51、50；lookup_code 的 income_type） |
| `amount` | integer | 是 | 給付額（元） |
| `residency` | string | 是 | 可選值：resident、nonresident |
| `nhi_insured` | boolean | 是 | 受領人是不是健保的保險對象（不是就不扣補充保費）；不確定就先問使用者 |
| `paid_by_insured_unit` | boolean |  | 是不是受領人所屬的投保單位給付；居住者薪資（代號 50）必填，其他預設否 |
| `salary_kind` | string |  | 薪資類：bonus 獎金、other 其他。居住者薪資（代號 50）必填：所屬投保單位給付的 other 是每月薪資（要帶 salary_method），不是所屬投保單位給付的 other 當兼職；獎金與兼職按每次給付 5%，不帶 salary_method、dependents；可選值：bonus、other |
| `salary_method` | string |  | 居住者每月薪資：table 查薪資扣繳稅額表（已填免稅額申報表）、flat 按全月給付總額 5%（沒填）；可選值：table、flat |
| `dependents` | integer |  | 查表用：配偶及受扶養親屬人數（配偶算 1，本人不算） |
| `insured_amount` | integer |  | 投保金額（所屬投保單位給付獎金時要） |
| `bonus_cumulative_before` | integer |  | 今年已給付的獎金累計，不含這一次（所屬投保單位給付獎金時要） |
| `date` | string |  | 有效日 YYYY-MM-DD，預設今天（台北） |
| `detail` | string |  | full＝params_used 每個參數附完整出處與法源（預設精簡，出處看 source_refs）；可選值：full |

## filing_calendar

列出某一年到期的申報與繳納期限，已套用政府辦公日曆的假日順延；附所屬月份、法源與出處；從事件起算的期限（例：給付日起 10 日內）在 other_deadlines。以 due_date 為準，不要拿 original_date 當期限。不確定期限落在哪個月就不帶 month，查整年再挑。個案的延期、展延核准不在這裡。

**輸入**

| 欄位 | 型別 | 必填 | 說明 |
|---|---|---|---|
| `year` | integer | 是 | 西元年，例 2026 |
| `entity_type` | string |  | 組織型態：company、sole_proprietorship、partnership、association、government_agency、individual；沒帶就全部 |
| `detail` | string |  | full＝回完整欄位（出處、查證日等）；預設精簡；可選值：full |
| `month` | integer |  | 只看這一年的這個月：以 due_date 的年月篩；原期限在這個月、順延到下個月的也列出，summary 開頭寫「原期限在本月，順延至 X 月 X 日」；最小 1；最大 12 |

## foreign_per_diem

查國外出差的生活費日支數額（美元／日，主計總處日支數額表，115 年 1 月 1 日生效）：輸入城市或國家（中英文，例：東京、Tokyo、日本），回表上的編號、國家、城市、日支數額（分季的列各段）與該國「其他」，附報支規則（查核準則第 74 條）。帶出差那一天 date 多回 on_date。大陸、港澳不在表內。

**輸入**

| 欄位 | 型別 | 必填 | 說明 |
|---|---|---|---|
| `place` | string | 是 | 城市或國家，例：東京、Tokyo、新加坡、美國 |
| `date` | string |  | 出差那一天（YYYY-MM-DD，選填）：帶了每筆多回 on_date，是那一天適用的日支數額（分季的照期間挑，表上沒列的期間用該國「其他」） |

## get_article

讀一條法規的原文：項款結構、每句的狀態（現行、歷年或過渡、已刪除）、修正日與出處。條號可寫「第二十四條之三」「24-3」。預設只回現行句，要歷年或過渡句帶 include_history。條文裡的數字只當佐證，引用數字用 get_tax_parameter。函釋與個案判斷不在這裡。

**輸入**

| 欄位 | 型別 | 必填 | 說明 |
|---|---|---|---|
| `law` | string | 是 | 法規名稱或 pcode |
| `article` | string｜integer | 是 | 條號（可以帶項款，例「第 24 條第 2 項第 1 款」） |
| `include_history` | boolean |  | 預設否 |
| `part` | integer |  | 長條文分段時取第幾段，預設 1；最小 1 |

## get_data_version

資料版本、建置時間、各類資料的筆數與最舊的查證日，以及維護者。

**輸入**：沒有參數。

## get_tax_parameter

查某一天有效的稅務參數（稅率、級距、門檻、限額比例），附生效期間、法源與出處。引用數字一律用這支，不要用條文裡的數字。不知道 id 先用 list_tax_parameters 找。

**輸入**

| 欄位 | 型別 | 必填 | 說明 |
|---|---|---|---|
| `id` | string | 是 | 參數 id（list_tax_parameters 查得到） |
| `date` | string |  | YYYY-MM-DD；沒帶就用台北時間的今天 |

## list_laws

列出收錄的法規：名稱、全國法規資料庫代碼、類別、修正日期、查證日、條數與官方連結。沒收錄的法規查不到，不代表沒有規定。

**輸入**

| 欄位 | 型別 | 必填 | 說明 |
|---|---|---|---|
| `category` | string |  | 類別（例 所得稅、營業稅） |
| `detail` | string |  | full＝回完整欄位（出處、查證日等）；預設精簡；可選值：full |

## list_tax_parameters

列出收錄的稅務參數（id、名稱、單位、有效期間），可用 query 篩（至少 2 個字）；用來找 get_tax_parameter 要用的 id。

**輸入**

| 欄位 | 型別 | 必填 | 說明 |
|---|---|---|---|
| `query` | string |  | 比對名稱與 id，至少 2 個字 |
| `detail` | string |  | full＝回完整欄位（出處、查證日等）；預設精簡；可選值：full |

## lookup_code

查代碼對照（扣繳所得類別、課稅別、發票格式代號、會計項目表兩版對照等），用代碼或名稱查，附出處。不認得的代碼回 not_found，不給最接近的。函釋與個案判斷不在這裡。

**輸入**

| 欄位 | 型別 | 必填 | 說明 |
|---|---|---|---|
| `kind` | string | 是 | 代碼種類 |
| `code` | string |  | 代碼（跟 name 二選一） |
| `name` | string |  | 名稱或其中幾個字（跟 code 二選一） |
| `date` | string |  | YYYY-MM-DD；帶了只回那一天適用的（例：會計項目表兩版） |

## payroll_guide

台灣的薪水、時薪、加班費、休息日與國定假日出勤、例假、天災停班（颱風假）、補休、最低工資、勞保健保勞退職災、二代健保、特休、資遣與預告工資、請假與產假、工讀生與部分工時的問題，不論多簡單，第一步先呼叫這支，讀完再用 calc_ 算（好幾個小問的關鍵字都放進 query）。回算薪水的固定做法（每小時工資額、倍率用分數、無條件進位）、條號、勞動部函釋與例題，並建議接著用哪支 calc_。入帳另用 bookkeeping_guide。

**輸入**

| 欄位 | 型別 | 必填 | 說明 |
|---|---|---|---|
| `query` | string |  | 問題或關鍵字，例：「工讀生 休息日 加班 9 小時」「颱風假 全勤」「資遣費 年資 平均工資」 |
| `section` | string |  | 指定段落的 id 或標題（目錄用 toc: true 取得） |
| `toc` | boolean |  | true＝回全部段落目錄（預設有找到段落就不回） |

## personal_tax_guide

台灣個人綜合所得稅（報稅、退稅補稅、免稅額、標準或列舉扣除額、特別扣除額、扶養、夫妻合併或分開計稅、股利 8.5% 或 28%、基本生活費差額、租金稿費退職所得、要不要申報、最低稅負）的問題，不論多簡單，第一步先呼叫這支，讀完再用 calc_personal_income_tax 算（好幾個小問的關鍵字都放進 query）。回固定做法（年度、擇優、扣除額、排富、基本生活費差額）、條號、財政部問答與常見錯誤。公司發薪與股利的扣繳入帳另用 payroll_guide、bookkeeping_guide。

**輸入**

| 欄位 | 型別 | 必填 | 說明 |
|---|---|---|---|
| `query` | string |  | 問題或關鍵字，例：「夫妻 薪資分開 計稅」「股利 28% 8.5%」「房租 扣除 排富」「基本生活費」 |
| `section` | string |  | 指定段落的 id 或標題（目錄用 toc: true 取得） |
| `toc` | boolean |  | true＝回全部段落目錄（預設有找到段落就不回） |

## property_tax_guide

台灣不動產與財產的稅（賣房子、房地合一、土地增值稅、地價稅、房屋稅、囤房稅、契稅、預售屋與紅單、遺產稅、贈與稅、繼承、過戶給子女）的問題，不論多簡單，第一步先呼叫這支，讀完再用 get_tax_parameter、lookup_code 查數字（好幾個小問的關鍵字都放進 query）。回固定做法（房地合一稅率與漲價總數額、土增稅與地價稅速算、房屋稅各縣市稅率、遺產稅與贈與稅免稅額扣除額級距）、條號與常見錯誤。公司帳上怎麼記另用 bookkeeping_guide。

**輸入**

| 欄位 | 型別 | 必填 | 說明 |
|---|---|---|---|
| `query` | string |  | 問題或關鍵字，例：「房地合一 持有 3 年 稅率」「土地增值稅 自用住宅 一生一屋」「房屋稅 新北市 3 戶」「遺產稅 扣除額 未成年」 |
| `section` | string |  | 指定段落的 id 或標題（目錄用 toc: true 取得） |
| `toc` | boolean |  | true＝回全部段落目錄（預設有找到段落就不回） |

## search_law

在收錄的法規全文用關鍵字找句子（多個關鍵字用空白隔開，每個都要命中；寫條號的排前面），回法規、條號、項款、句子、狀態與出處。預設不回歷年或過渡句。只查收錄的法規，查不到不代表沒有規定。條文裡的數字只當佐證，引用數字用 get_tax_parameter。函釋與個案判斷不在這裡。

**輸入**

| 欄位 | 型別 | 必填 | 說明 |
|---|---|---|---|
| `query` | string | 是 | 關鍵字，至少 2 個字 |
| `law` | string |  | 只查這一部（名稱或 pcode） |
| `limit` | integer |  | 預設 10、最多 30；最小 1；最大 30 |
| `include_history` | boolean |  | 要不要包含歷年或過渡的句子，預設否 |

## topic_map

依問題類型（扣繳、營業稅、捐贈、開公司等）列出該查哪幾部法規的哪幾條、為什麼、別漏的點；再用 get_article 讀條文。函釋與個案判斷不在這裡。

**輸入**

| 欄位 | 型別 | 必填 | 說明 |
|---|---|---|---|
| `topic` | string | 是 | 主題或問題類型 |
