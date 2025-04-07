from datetime import datetime
import json
from pathlib import Path

LOG_DIR = Path("logs/memory_journal")
LOG_DIR.mkdir(parents=True, exist_ok=True)

def log_thought(clone_id, text):
    log_file = LOG_DIR / f"{clone_id}.jsonl"
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "thought": text
    }
    with open(log_file, "a") as f:
        f.write(json.dumps(entry) + "\n")