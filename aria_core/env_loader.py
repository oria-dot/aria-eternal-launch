import os
from pathlib import Path

def load_env():
    env_path = Path(".env")
    if env_path.exists():
        with env_path.open("r") as f:
            for line in f:
                if "=" in line and not line.startswith("#"):
                    key, val = line.strip().split("=", 1)
                    os.environ.setdefault(key, val)