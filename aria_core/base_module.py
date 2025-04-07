class BaseModule:
    def __init__(self, config=None):
        self.config = config or {}

    def run(self):
        raise NotImplementedError("Each module must implement a run() method")