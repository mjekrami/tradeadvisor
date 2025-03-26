import logging
from langchain_community.utilities import SearxSearchWrapper
from langchain.tools import tool

logger = logging.getLogger(__name__)

searx = SearxSearchWrapper(searx_host="http://localhost:888", k=10)


@tool("search_web")
def search_web(query):
    """Searches the web using Searxng tool by providing the search query"""
    results = searx.run(query, engines=["wiki"])
    return results


@tool("search_news")
def search_news(query):
    """Searches for latest news (NOT OLDER THAN 3 MONTHS) from specific websites"""
    results = searx.run(query, engines=["crypto_news"])
    return results
