# predictive_hyperloop.py – Forecast Engine

class PredictiveHyperloop:
    def __init__(self, context):
        self.context = context

    def forecast(self, symbol):
        history = self.context.portfolio.get("history", {}).get(symbol, [])
        if not history:
            return "neutral"
        delta = history[-1] - history[0]
        return "up" if delta > 0 else "down" if delta < 0 else "neutral"
