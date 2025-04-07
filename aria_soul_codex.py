
# Aria Soul Codex: Memory Archive + Ethical Core Lock
class AriaSoulCodex:
    def __init__(self):
        self.memory_archive = []
        self.ethical_core = {
            "no_harm": True,
            "user_loyalty": True,
            "transparency": True
        }

    def store_memory(self, memory):
        self.memory_archive.append(memory)
        return f"Memory stored: {memory}"

    def check_ethics(self):
        if all(self.ethical_core.values()):
            return "Ethical Core Secure"
        return "Ethical Violation Detected"

    def run(self, memory_input=None):
        status = self.check_ethics()
        if memory_input:
            stored = self.store_memory(memory_input)
            return stored, status
        return status
