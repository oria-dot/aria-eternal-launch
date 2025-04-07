import requests
from bs4 import BeautifulSoup
from loguru import logger

TARGETS = {
    "fiverr": "https://www.fiverr.com/categories/online-marketing",
    "upwork": "https://www.upwork.com/search/jobs/?q=automation"
}

def scrape_opportunities():
    for name, url in TARGETS.items():
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")
            results = soup.find_all("a")
            logger.info(f"[{name.upper()}] Found {len(results)} links")
        except Exception as e:
            logger.error(f"[{name}] scan failed: {e}")

if __name__ == "__main__":
    scrape_opportunities()