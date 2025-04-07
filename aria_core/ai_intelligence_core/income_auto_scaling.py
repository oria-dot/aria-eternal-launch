# income_auto_scaling.py – Scales income streams based on performance

class IncomeAutoScaling:
    def __init__(self, context):
        self.context = context

    def scale_income(self):
        income = self.context.income
        for stream, value in income.items():
            if value < 1000 and stream != "gumroad":  # Skip gumroad as a static income
                income[stream] = value * 1.2  # Scale income streams that are below 1000
                print(f"[Income Auto-Scaling] Scaling {stream} by 20%. New value: {income[stream]}")
            else:
                print(f"[Income Auto-Scaling] {stream} stable at {value}")
        return income
