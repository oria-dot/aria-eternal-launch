
from concurrent.futures import ThreadPoolExecutor

class ParallelExecutor:
    def __init__(self, context):
        self.context = context
        self.executor = ThreadPoolExecutor(max_workers=5)

    def submit_task(self, func, *args):
        return self.executor.submit(func, *args)
