# council_protocol.py – Multi-Agent Voting + Decision System

class AICouncilProtocol:
    def __init__(self, context, modules):
        self.context = context
        self.modules = modules
        self.votes = {}

    def run_vote(self, topic="market_action"):
        self.votes.clear()
        for mod in self.modules:
            name = mod.__class__.__name__
            try:
                if hasattr(mod, "vote"):
                    self.votes[name] = mod.vote(topic)
            except Exception as e:
                self.votes[name] = f"error: {e}"

        self.context.strategy["council_vote"] = self.votes
        return self.votes

    def summarize(self):
        from collections import Counter
        decision = Counter(self.votes.values())
        top = decision.most_common(1)
        return top[0] if top else ("no consensus", 0)
