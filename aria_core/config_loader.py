import yaml
import os
from loguru import logger

CONFIG_PATH = os.getenv("ARIA_CONFIG_PATH", "config/aria_config.yaml")

REQUIRED_KEYS = {
    "mode": str,
    "logging": dict,
    "modules": dict
}

def load_and_validate_config():
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError(f"Config file not found: {CONFIG_PATH}")
    
    with open(CONFIG_PATH, "r") as f:
        config = yaml.safe_load(f)

    for key, val_type in REQUIRED_KEYS.items():
        if key not in config or not isinstance(config[key], val_type):
            raise ValueError(f"Invalid or missing config key: {key}")

    logger.info("ARIA config validated.")
    return config