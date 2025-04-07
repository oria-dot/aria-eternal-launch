# income_optimizer.py – Maximizes income sources across freelance, SaaS, affiliate

class IncomeOptimizer:
    def __init__(self, context):
        self.context = context

    def evaluate_streams(self):
        income = self.context.income or {
            "freelance": 1200,
            "affiliate": 850,
            "saas": 1800,
            "gumroad": 600
        }
        suggestions = {}
        for stream, value in income.items():
            if value < 1000:
                suggestions[stream] = "Scale Up"
            else:
                suggestions[stream] = "Stable"

        self.context.income["recommendations"] = suggestions
        return suggestions
