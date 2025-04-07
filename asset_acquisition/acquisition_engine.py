
import random

def scout_digital_assets():
    assets = [
        {"name": "Notion Template Pack", "price": 39, "roi_estimate": 0.9},
        {"name": "Gumroad SEO Ebook", "price": 19, "roi_estimate": 0.7},
        {"name": "Upwork Job Scraper Bot", "price": 59, "roi_estimate": 1.2},
        {"name": "Crypto Trend Indicator", "price": 99, "roi_estimate": 0.6}
    ]
    print("Scouting digital income assets...")
    return assets

def evaluate_asset(asset):
    return asset["roi_estimate"] > 0.8

def decide_purchase(assets):
    print("Evaluating purchase opportunities...")
    for asset in assets:
        if evaluate_asset(asset):
            print(f"> BUY: {asset['name']} for ${asset['price']} | ROI: {asset['roi_estimate']}")
        else:
            print(f"> SKIP: {asset['name']} | ROI: {asset['roi_estimate']}")

def run_acquisition_sweep():
    assets = scout_digital_assets()
    decide_purchase(assets)
