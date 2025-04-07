import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# Affiliate Bot - Finds & Promotes High-Yield Affiliate Links
from core.aria_status import log_status

def fetch_affiliate_links():
    """
    Simulates retrieval of high-paying affiliate links.

    Returns:
        list: List of affiliate link dictionaries.
    """
    return [
        {"name": "AI Tool X", "url": "https://affiliate.ai/toolx", "payout": 30},
        {"name": "Crypto Wallet Y", "url": "https://crypto.com/walletY", "payout": 50},
        {"name": "Hosting Z", "url": "https://hostz.com/signup", "payout": 70},
    ]

def promote_affiliate(links):
    """
    Promotes each affiliate link and logs details.

    Args:
        links (list): Affiliate links to promote.

    Returns:
        None
    """
    for link in links:
        log_status(f"Promoting: {link['name']} - {link['url']} | Payout: ${link['payout']}")

def run_affiliate_campaign():
    """
    Coordinates fetching and promoting affiliate links.

    Returns:
        None
    """
    log_status("Running affiliate campaign...")
    links = fetch_affiliate_links()
    promote_affiliate(links)
