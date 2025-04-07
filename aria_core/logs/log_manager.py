
import logging
from logging.handlers import RotatingFileHandler

class LogManager:
    def __init__(self, log_path="aria_system.log"):
        self.logger = logging.getLogger("ARIA")
        handler = RotatingFileHandler(log_path, maxBytes=5*1024*1024, backupCount=3)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def log_event(self, message):
        self.logger.info(message)
