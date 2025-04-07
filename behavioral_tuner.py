# behavioral_tuner.py – Auto-adjust Strategy & Clone Logic Based on Memory

class BehavioralTuner:
    def __init__(self, memory_engine, feedback_core):
        self.memory = memory_engine
        self.feedback = feedback_core

    def tune_strategy(self, symbol):
        analysis = self.feedback.analyze_symbol(symbol)
        new_mode = analysis["strategy_trend"]
        return f"{symbol} → Strategy Recommendation: {new_mode.upper()} (Avg PnL: {analysis['avg_pnl']})"

    def build_avoid_list(self, threshold=-4.5):
        return list(set([
            entry["symbol"]
            for entry in self.memory.log
            if entry["pnl"] is not None and entry["pnl"] < threshold
        ]))

    def get_tuning_report(self, symbols):
        report = []
        for sym in symbols:
            report.append(self.tune_strategy(sym))
        return report
