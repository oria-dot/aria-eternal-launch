# llm_agent.py – Aria's Decision Agent powered by LLMs

class LLMDecisionAgent:
    def __init__(self, context):
        self.context = context

    def reason_about_market(self, signal):
        try:
            # Example of signal input:
            # {"sentiment": 0.45, "trend": "up", "volatility": "medium"}

            sentiment = signal.get("sentiment", 0)
            trend = signal.get("trend", "neutral")
            volatility = signal.get("volatility", "medium")

            # Basic AI-style logic (can be replaced with real OpenAI/LLM chain)
            thought = f"Trend: {trend}, Sentiment: {sentiment}, Volatility: {volatility}"

            if trend == "up" and sentiment > 0.3:
                decision = "BUY"
            elif trend == "down" and sentiment < -0.3:
                decision = "SELL"
            else:
                decision = "HOLD"

            return {
                "thought": thought,
                "decision": decision
            }

        except Exception as e:
            return {
                "thought": f"LLM Agent encountered error: {str(e)}",
                "decision": "HOLD"
            }
