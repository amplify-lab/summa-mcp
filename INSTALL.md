# 安裝說明（給 AI 助理照著做）

使用者請你安裝 Summa 免費會計助手時，照下面判斷用戶端，逐步執行。伺服器網址是 `https://mcp.summa.com.tw/mcp`，公開、不用登入、不用金鑰。

## 1. 判斷用戶端

- 你能執行終端機指令（例如 Claude Code）：照第 2 節。
- 你不能執行指令（Claude 網頁版、桌面版）：照第 3 節，把步驟一條一條告訴使用者。
- 你是 ChatGPT：照第 3b 節，把步驟一條一條告訴使用者。

## 2. Claude Code

2-1. 加 MCP 伺服器（你可以自己執行）：

```
claude mcp add --transport http summa-tw-accounting https://mcp.summa.com.tw/mcp
```

2-2. 確認：

- 請使用者重新開啟 Claude Code。
- 輸入 `/mcp`，應看到 `summa-tw-accounting` 已連線。
- 問一句「營業稅一般稅率是多少？附出處」，回答應附營業稅法第 10 條與生效日。


## 3. Claude 網頁版與桌面版（請使用者操作）

1. Claude 設定 › 連接器（Connectors）› 新增自訂連接器。
2. 名稱：`Summa 免費會計助手`
3. 網址：`https://mcp.summa.com.tw/mcp`
4. 按新增。
5. 開新對話問「營業稅一般稅率是多少？附出處」，回答應附營業稅法第 10 條與生效日。


## 3b. ChatGPT（請使用者操作）

1. 確認：只有網頁版；Plus、Pro、Business、Enterprise、Edu 可以用，Business、Enterprise、Edu 要管理員開放；免費版不能加。
2. 設定 › 安全與登入（Security and login）› 打開「開發者模式」（Developer mode）。
3. 到 Plugins（https://chatgpt.com/plugins ）按＋，新增開發者模式的 app：名稱 `Summa 免費會計助手`，網址 `https://mcp.summa.com.tw/mcp`，驗證選「不需驗證」（No Authentication）。
4. 對話時從輸入框的＋選單打開開發者模式，選這個 app。
5. 問「營業稅一般稅率是多少？附出處」確認。


## 4. 其他 MCP 用戶端

加一個 streamable HTTP 類型的 MCP 伺服器，網址 `https://mcp.summa.com.tw/mcp`，不用認證。

## 5. 更新

伺服器端的資料由 Summa 持續更新，使用者不用做任何事。`get_data_version` 可以查目前的資料版本與查證日。
