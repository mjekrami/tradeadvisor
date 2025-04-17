from config import CONFIG
from langchain.tools import tool
from langchain_community.utilities.alpha_vantage import AlphaVantageAPIWrapper

alpha_vantage = AlphaVantageAPIWrapper(
    alpha_vantage_api_key=CONFIG.tool_config["alpha_vantage"]["api_key"]
)


@tool("market_sentiment")
def get_market_seniment(symbol):
    """Gets latest market sentiment news about a pair or symbol of cryptocurrency from alpha vantage"""
    data = alpha_vantage._get_market_news_sentiment(symbol)
    return data

