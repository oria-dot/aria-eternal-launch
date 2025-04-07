import openai
import os
from loguru import logger

class LLMDecisionAgent:
    def __init__(self, model="gpt-4-turbo", api_key=None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model = model
        openai.api_key = self.api_key

    def reason_about_market(self, signal_data):
        try:
            messages = [
                {"role": "system", "content": "You are a market decision-making AI assistant."},
                {"role": "user", "content": f"Analyze the following signal data and decide whether to BUY, HOLD, or SELL:"
{signal_data}"}"
            ]
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages
            )

            content = response["choices"][0]["message"]["content"]
            return {
                "thought": f"LLM Response: {content}",
                "decision": content.strip().split()[0].upper()  # naive first-word command
            }
        except Exception as e:
            logger.error(f"LLM agent failed: {e}")
            from aria_core.memory_core.gpt_snapshot_writer import save_gpt_thought
        save_gpt_thought(content, decision=content.strip().split()[0].upper())
        return {"thought": "LLM unavailable", "decision": "HOLD"}