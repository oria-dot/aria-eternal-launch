# strategy_reflex.py – Adaptive Trading Strategy Engine with LLM

try:
    from aria_core.ai_intelligence_core.llm_agent import LLMDecisionAgent
except ImportError:
    # Fallback for testing
    class LLMDecisionAgent:
        def __init__(self, context):
            self.context = context

        def reason_about_market(self, signal):
            return {
                "thought": "LLM not available — using fallback logic.",
                "decision": "HOLD"
            }

class StrategyReflexEngine:
    def __init__(self, context):
        self.context = context

    def generate_signal(self, symbol):
        try:
            # Load market signals for the symbol
            signals = self.context.get("signals", {}).get(symbol, {})
            trend = signals.get("trend", "neutral")
            sentiment = signals.get("sentiment", 0)

            # Use LLM for enhanced reasoning
            agent = LLMDecisionAgent(self.context)
            result = agent.reason_about_market(signals)
            print("LLM Decision Thought:", result.get("thought"))

            return result.get("decision", "HOLD")

        except Exception as e:
            print(f"[StrategyReflexEngine Error]: {e}")

            # Fallback logic
            if trend == "up" and sentiment > 0.3:
                return "BUY"
            elif trend == "down" and sentiment < -0.3:
                return "SELL"
            return "HOLD"
