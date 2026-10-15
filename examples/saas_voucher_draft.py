# 範例：電商 SaaS 後台把一筆平台撥款做成傳票草稿，交給會計審核。
# 你自己的資料（撥款明細）是一支 function tool；記法、科目、稅額查 Summa 免費會計助手（MCP 工具轉成 function tool）。
#
# 需要：Python 3.10 以上、pip install "anthropic[mcp]"、環境變數 ANTHROPIC_API_KEY
# 執行：python saas_voucher_draft.py
import asyncio
import json

from anthropic import AsyncAnthropic, beta_async_tool
from anthropic.lib.tools.mcp import async_mcp_tool
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

SUMMA_MCP = "https://mcp.summa.com.tw/mcp"

SYSTEM = """你是台灣公司的會計助理。
- 記法、科目、稅率、期限一律先用 Summa 免費會計助手的工具查，不要憑記憶。
- 產出傳票草稿：日期、借貸科目、金額、摘要，借貸要相等；附上依據（法規條號）。
- 草稿由會計審核後才入帳，資料不足就列出要補什麼。"""


@beta_async_tool
async def get_payout(payout_id: str) -> str:
    """讀取電商平台的撥款明細（訂單金額、平台手續費、實際撥款）。

    Args:
        payout_id: 撥款單號，例如 P-20261015-001
    """
    # 範例資料；實際從你的資料庫或平台 API 讀
    return json.dumps(
        {
            "payout_id": payout_id,
            "date": "2026-10-15",
            "orders_total_incl_tax": 52500,  # 本期訂單含稅金額，發票已在出貨時開立
            "platform_fee_incl_tax": 3150,  # 平台手續費，平台開立發票給賣家
            "paid_to_bank": 49350,
        },
        ensure_ascii=False,
    )


async def main() -> None:
    client = AsyncAnthropic()
    async with streamable_http_client(SUMMA_MCP) as (read, write):
        async with ClientSession(read, write) as mcp:
            await mcp.initialize()
            summa_tools = [async_mcp_tool(t, mcp) for t in (await mcp.list_tools()).tools]

            runner = client.beta.messages.tool_runner(
                model="claude-opus-5-5",
                max_tokens=16000,
                system=SYSTEM,
                tools=[get_payout, *summa_tools],
                # 模型拒答時由伺服器自動換模型重跑
                betas=["server-side-fallback-2026-07-01"],
                fallbacks="default",
                messages=[{"role": "user", "content": "撥款單 P-20261015-001 入帳了，幫我做傳票草稿。"}],
            )
            async for message in runner:
                for block in message.content:
                    if block.type == "tool_use":
                        print(f"→ 呼叫 {block.name}")
                    elif block.type == "text":
                        print(block.text)


if __name__ == "__main__":
    asyncio.run(main())
