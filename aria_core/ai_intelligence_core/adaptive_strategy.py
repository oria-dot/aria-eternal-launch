# adaptive_strategy.py – Dynamic strategy adjustments based on market data

class AdaptiveStrategyAdjustment:
    def __init__(self, context):
        self.context = context

    def adjust_strategy(self):
        performance = self.context.strategy.get("scores", {})
        if not performance:
            print("[Adaptive Strategy] No performance data.")
            return

        # Adjust strategy based on performance scores
        for module, score in performance.items():
            if score < 50:
                print(f"[Adaptive Strategy] Adjusting {module} strategy.")
                self.context.strategy[module] = "recalibrate"
            else:
                self.context.strategy[module] = "stable"
