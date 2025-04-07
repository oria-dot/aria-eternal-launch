import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# Affiliate Product Scraper - Discovers Trending Digital Goods
from core.aria_status import log_status

def scrape_hot_products():
    """
    Simulates scraping hot trending affiliate products.

    Returns:
        list: List of popular affiliate products.
    """
    products = [
        {"product": "ChatGPT Templates", "platform": "Gumroad"},
        {"product": "Crypto Staking Guide", "platform": "Etsy"}
    ]
    log_status("Scraped trending affiliate products.")
    return products
