# learning_feedback_loop.py – Self-Optimizing AI Strategy Evaluator

class LearningFeedbackLoop:
    def __init__(self, context, memory_engine):
        self.context = context
        self.memory = memory_engine

    def evaluate_strategies(self):
        performance_log = self.memory.db
        scores = {}

        for module, entries in performance_log.items():
            success = sum(1 for e in entries if "success" in e["outcome"])
            total = len(entries)
            if total > 0:
                score = round((success / total) * 100, 2)
                scores[module] = score

        self.context.strategy["scores"] = scores
        return scores
