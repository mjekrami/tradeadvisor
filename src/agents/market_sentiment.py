from llms import akash_llm
from tools import search_news, search_web
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent

MARKET_SENTMENT_PROMPT = """
    1. Review the latest financial news from leading sources like Bloomberg, CNBC, CoinDesk, etc., regarding {input}'s market sentiment. Is the sentiment currently bullish, bearish, or neutral?
    2. Monitor crypto news websites for trends and discussions around {input}. Is the sentiment on these platforms aligned with the broader financial market outlook?
    3. Search for any major news events or economic announcements in the next 24 hours that could impact {input}'s price. Are there any upcoming government regulations, ETF approvals, or major economic data releases that might drive volatility?
"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", MARKET_SENTMENT_PROMPT),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)


def create_market_sentiment_agent():
    tools = [search_news, search_web]
    agent = create_tool_calling_agent(akash_llm, tools, prompt)
    return agent
