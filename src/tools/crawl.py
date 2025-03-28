import os
from config import get_tools_config
from langchain_community.document_loaders.firecrawl import FireCrawlLoader
from langchain.tools import tool


api_key = get_tools_config("firecrawl", "api_key")
url = get_tools_config("firecrawl", "url")
loader = FireCrawlLoader(api_key=api_key, url=url, mode="scrape")


@tool("scrape_website")
def scrape_website(website):
    """Scrapes a webpage of a website"""
    pass
