# context.py – Singleton Shared Context

from dataclasses import dataclass, field
import threading

@dataclass
class AriaContext:
    memory: list = field(default_factory=list)
    signals: dict = field(default_factory=dict)
    portfolio: dict = field(default_factory=dict)
    status: list = field(default_factory=list)
    strategy: dict = field(default_factory=dict)
    emotions: list = field(default_factory=list)
    command_tree: list = field(default_factory=list)

    _instance = None
    _lock = threading.Lock()

    @classmethod
    def get(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = cls()
            return cls._instance
