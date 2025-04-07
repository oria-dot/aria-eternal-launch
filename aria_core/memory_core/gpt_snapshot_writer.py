import json
from datetime import datetime
from pathlib import Path

SNAPSHOT_FILE = Path("aria_core/memory_core/gpt_knowledge_base.json")

def save_gpt_thought(thought, decision=None, strategy=None):
    snapshot = json.load(SNAPSHOT_FILE.open())
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "thought": thought,
        "decision": decision,
        "strategy": strategy
    }
    if decision:
        snapshot["decisions"].append(entry)
    if strategy:
        snapshot["strategies"].append(entry)
    snapshot["logs"].append(entry)
    with open(SNAPSHOT_FILE, "w") as f:
        json.dump(snapshot, f, indent=2)