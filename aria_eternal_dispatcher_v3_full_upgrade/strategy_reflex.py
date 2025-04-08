
class StrategyReflexEngine:
    def __init__(self, context):
        self.context = context

    def generate_signal(self, symbol):
        signals = self.context.get('signals', {}).get(symbol, {})
        trend = signals.get("trend", "neutral")
        sentiment = signals.get("sentiment", 0)

        if trend == "up" and sentiment > 0.3:
            return "BUY"
        elif trend == "down" and sentiment < -0.3:
            return "SELL"
        return "HOLD"
