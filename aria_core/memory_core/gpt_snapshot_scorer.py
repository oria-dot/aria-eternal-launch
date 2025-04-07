import json
from pathlib import Path
from datetime import datetime

SNAPSHOT_PATH = Path("aria_core/memory_core/gpt_knowledge_base.json")

def record_strategy_score(strategy_text, score):
    with open(SNAPSHOT_PATH, "r") as f:
        data = json.load(f)

    for entry in data.get("strategies", []):
        if entry["strategy"] == strategy_text:
            if "scores" not in entry:
                entry["scores"] = []
            entry["scores"].append({
                "timestamp": datetime.utcnow().isoformat(),
                "value": score
            })

    with open(SNAPSHOT_PATH, "w") as f:
        json.dump(data, f, indent=2)