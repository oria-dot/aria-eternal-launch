import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# Affiliate AutoPoster - Automatically Shares to Platforms
from core.aria_status import log_status

def autopost_to_platforms(content):
    """
    Simulates posting affiliate content to multiple social platforms.

    Args:
        content (str): Promotional content to post.

    Returns:
        None
    """
    platforms = ["Twitter", "Reddit", "Medium"]
    for platform in platforms:
        log_status(f"Auto-posting to {platform}: {content}")
