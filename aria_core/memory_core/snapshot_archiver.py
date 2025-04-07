import shutil
from datetime import datetime
from pathlib import Path

def archive_snapshot():
    src = Path("aria_core/memory_core/gpt_knowledge_base.json")
    if not src.exists():
        print("No snapshot to archive.")
        return

    date_str = datetime.utcnow().strftime("%Y-%m-%d")
    dest = Path("aria_core/memory_core/archives")
    dest.mkdir(parents=True, exist_ok=True)
    target = dest / f"gpt_knowledge_base_{date_str}.json"
    shutil.copy(src, target)
    print(f"Snapshot archived to: {target}")