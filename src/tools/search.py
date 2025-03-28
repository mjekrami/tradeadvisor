import logging
from config import get_tools_config
from langchain_community.utilities import SearxSearchWrapper
from langchain.tools import tool

logger = logging.getLogger(__name__)

searx = SearxSearchWrapper(searx_host=get_tools_config("searxng", "host"), k=10)


@tool("search_web")
def search_web(query):
    """Searches the web using Searxng tool by providing the search query"""
    results = searx.run(query, engines=["wiki"])
    logger.info(f"Results from search_web tool: {query}\n{results}")
    return results


@tool("search_news")
def search_news(query):
    """Searches for latest news (NOT OLDER THAN 3 MONTHS) from specific websites"""
    results = searx.run(query, engines=["crypto_news"])
    logger.info(f"Results from search_news tool: {query}\n{results}")
    return results
