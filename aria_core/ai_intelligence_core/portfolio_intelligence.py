# portfolio_intelligence.py – Portfolio Allocator and Risk Adjuster

class PortfolioIntelligence:
    def __init__(self, context):
        self.context = context

    def optimize(self):
        cash = self.context.portfolio.get("cash", 10000)
        positions = self.context.portfolio.get("positions", {})
        if not positions:
            self.context.portfolio["positions"] = {"AAPL": cash * 0.5, "GOOG": cash * 0.5}
        else:
            for k in positions:
                positions[k] *= 1.01  # simple simulated growth
        return self.context.portfolio
