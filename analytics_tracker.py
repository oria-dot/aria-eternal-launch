# analytics_tracker.py – Aria Profit + Clone ROI Analytics

import random

class AnalyticsTracker:
    def __init__(self):
        self.income_sources = {
            "freelance": random.randint(300, 800),
            "gumroad": random.randint(100, 400),
            "saas": random.randint(200, 600)
        }
        self.cost_per_clone = 20  # USD/month assumed

    def get_total_income(self):
        return sum(self.income_sources.values())

    def get_clone_roi(self, active_clones):
        roi_data = []
        for clone in active_clones:
            profit = random.randint(30, 150)
            roi = round((profit - self.cost_per_clone) / self.cost_per_clone * 100, 2)
            roi_data.append({
                "clone_id": clone["id"],
                "role": clone["role"],
                "region": clone["region"],
                "roi_percent": roi
            })
        return roi_data

    def run(self, active_clones=[]):
        return {
            "total_income": self.get_total_income(),
            "clone_roi": self.get_clone_roi(active_clones)
        }
