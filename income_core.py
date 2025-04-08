# Income Automation Core (Upgraded)

import csv
from datetime import datetime

class IncomeAutomationCore:
    def __init__(self, strategy="balanced"):
        self.sources = {
            "Freelance": 0,
            "Gumroad": 0,
            "SaaS": 0,
            "CloneOps": 0
        }
        self.total_income = 0
        self.distribution = {
            "reinvest": 0,
            "savings": 0,
            "operations": 0
        }
        self.strategy = strategy

    def add_income(self, source, amount):
        if source in self.sources:
            self.sources[source] += amount
        else:
            self.sources[source] = amount
        self.total_income += amount
        self._log_income(source, amount)

    def _log_income(self, source, amount):
        with open("income_log.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), source, amount])

    def auto_distribute(self):
        if self.strategy == "aggressive":
            reinvest_ratio = 0.6
        elif self.strategy == "conservative":
            reinvest_ratio = 0.2
        else:
            reinvest_ratio = 0.4  # balanced

        self.distribution["reinvest"] = round(self.total_income * reinvest_ratio, 2)
        self.distribution["savings"] = round(self.total_income * 0.3, 2)
        self.distribution["operations"] = round(self.total_income * (1 - reinvest_ratio - 0.3), 2)
        return self.distribution

    def get_income_summary(self):
        return {
            "sources": self.sources,
            "total_income": self.total_income,
            "distribution": self.distribution,
            "strategy": self.strategy
        }

    def run(self):
        return self.auto_distribute()
