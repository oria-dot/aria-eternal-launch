# memory_core.py – Persistent Memory Logger

import json, os
from datetime import datetime

class MemoryEngine:
    def __init__(self, context, path="aria_core/logs/memory_log.json"):
        self.context = context
        self.path = path
        self._load()

    def _load(self):
        if os.path.exists(self.path):
            with open(self.path, "r") as f:
                self.db = json.load(f)
        else:
            self.db = {}

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.db, f, indent=2)

    def log(self, module, action, outcome):
        timestamp = datetime.now().isoformat()
        self.db.setdefault(module, []).append({
            "timestamp": timestamp,
            "action": action,
            "outcome": outcome
        })
        self.save()
