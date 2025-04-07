import json
import random
from pathlib import Path
from loguru import logger

SNAPSHOT_PATH = Path("aria_core/memory_core/gpt_knowledge_base.json")

from aria_core.memory_core.clone_journal import log_thought
from aria_core.memory_core.gpt_snapshot_scorer import record_strategy_score

class Clone:
    def __init__(self, id, strategy, origin="snapshot"):
        self.id = id
        self.strategy = strategy
        self.origin = origin
        self.performance = 0.0

    def run(self):
        logger.info(f"[{self.id}] Executing strategy from {self.origin}: {self.strategy}")
        log_thought(self.id, f"Strategy used: {self.strategy}")
        # Simulated behavior
        self.performance = random.uniform(0.1, 1.0)
        log_thought(self.id, f"Performance score: {self.performance:.2f}")
        record_strategy_score(self.strategy, self.performance)
        return self.performance

def spawn_clone_from_snapshot(index=None):
    with open(SNAPSHOT_PATH) as f:
        data = json.load(f)

    if not data["strategies"]:
        raise ValueError("No GPT strategies in snapshot!")

    strat = random.choice(data["strategies"]) if index is None else data["strategies"][index]
    clone_id = f"Clone_{random.randint(1000, 9999)}"
    clone = Clone(id=clone_id, strategy=strat["strategy"])
    clone.run()
    return clone

if __name__ == "__main__":
    clone = spawn_clone_from_snapshot()
    logger.info(f"[{clone.id}] Finished with performance {clone.performance:.2f}")