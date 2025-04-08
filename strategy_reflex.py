from aria_core.ai_intelligence_core.llm_agent import LLMDecisionAgent
# strategy_reflex.py – Adaptive Trading Strategy Engine

class StrategyReflexEngine:
    def __init__(self, context):
        self.context = context

    def generate_signal(self, symbol):
        agent = LLMDecisionAgent(self.context)
        result = agent.reason_about_market(self.context.get('signals', {}).get(symbol, {}))
        print(result['thought'])
self, symbol)
:
        # Placeholder: insert real logic using sentiment, trend, volatility
        signals = self.context.signals.get(symbol, {})
        trend = signals.get("trend", "neutral")
        sentiment = signals.get("sentiment", 0)

        if trend == "up" and sentiment > 0.3:
            return "BUY"
        elif trend == "down" and sentiment < -0.3:
            return "SELL"
        return "HOLD"
