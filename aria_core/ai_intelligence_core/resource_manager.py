
import psutil

class ResourceManager:
    def __init__(self):
        self.cpu_threshold = 80  # Percentage CPU load threshold

    def check_cpu_usage(self):
        cpu_usage = psutil.cpu_percent(interval=1)
        return cpu_usage < self.cpu_threshold
