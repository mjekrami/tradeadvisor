from config import config
from langchain_community.document_loaders.firecrawl import FireCrawlLoader
from langchain.tools import tool

api_key = "" if not config.get_tools_config("firecrawl", "firecrawl_api_key") else ""
url = config.get_tools_config("firecrawl", "firecrawl_url")

loader = FireCrawlLoader(api_key=api_key, url=url, mode="scrape")


@tool("scrape_website")
def scrape_website(website):
    """Scrapes a webpage of a website"""
    pass
