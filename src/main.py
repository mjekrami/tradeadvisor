from langchain.agents import AgentExecutor
from config import CONFIG
from tools import search_news
from llms import get_llm
from agents import get_agent

market_sentiment_config = CONFIG.agent_config["market_sentiment"]

llm = get_llm(market_sentiment_config["llm"])
market_sentiment = get_agent("market_sentiment", llm)

agent_executor = AgentExecutor(agent=market_sentiment, tools=[search_news])

output = agent_executor.invoke({"input": "btc"})
print(output)
