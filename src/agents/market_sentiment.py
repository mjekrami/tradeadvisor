from tools import search_web
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import Tool
from langchain.agents import create_tool_calling_agent

MARKET_SENTMENT_PROMPT = """
    1. Search on the web for news from leading sources like Bloomberg, CNBC, CoinDesk, etc., regarding {input}'s market sentiment. Is the sentiment currently bullish, bearish, or neutral?
    2. Monitor crypto news websites for trends and discussions around {input}. Is the sentiment on these platforms aligned with the broader financial market outlook?
    3. Search for any major news events or economic announcements in the next 24 hours that could impact {input}'s price. Are there any upcoming government regulations, ETF approvals, or major economic data releases that might drive volatility?
"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", MARKET_SENTMENT_PROMPT),
        (
            "human",
            """
        {input} market sentiment
        """,
        ),
        ("placeholder", "{agent_scratchpad}"),
    ]
)


def create_market_sentiment_agent(llm):
    agent = create_tool_calling_agent(
        llm,
        tools=[
            Tool(
                name="Search Web",
                func=search_web,
                description="Use it for searching the web",
            )
        ],
        prompt=prompt,
    )
    return agent
