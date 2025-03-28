from llms import akash_llm
from tools import populate_indicator, fetch_crypto_price
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent

PROBABILITY_ASSISTANCE_PROMPT = """
Based on the combined technical analysis and market sentiment provided, assess the probability of a successful Long position for {input}. Consider fetching the price and 
using tools such as RSI, MACD, chart patterns, and news sentiment.
Provide the reasoning for the probability assessments of Long and Short positions. What are the key technical indicators and sentiment factors influencing these probabilities?
"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", PROBABILITY_ASSISTANCE_PROMPT),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)


def create_market_sentiment_agent():
    tools = [populate_indicator, fetch_crypto_price]
    agent = create_tool_calling_agent(akash_llm, tools, prompt)
    return agent
