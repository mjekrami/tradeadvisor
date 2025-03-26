from langchain.agents import Agent

MARKET_SENTMENT_PROMPT = """
    1. Review the latest financial news from leading sources like Bloomberg, CNBC, CoinDesk, etc., regarding Bitcoin's market sentiment. Is the sentiment currently bullish, bearish, or neutral?
    2. Monitor crypto news websites for trends and discussions around Bitcoin. Is the sentiment on these platforms aligned with the broader financial market outlook?
    3. Search for any major news events or economic announcements in the next 24 hours that could impact Bitcoin's price. Are there any upcoming government regulations, ETF approvals, or major economic data releases that might drive volatility?
"""
