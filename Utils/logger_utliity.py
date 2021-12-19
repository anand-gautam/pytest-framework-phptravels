import logging
from datetime import datetime
import os

class GenerateLog:
    @staticmethod
    def create_log():
        cur_date = datetime.strftime(datetime.now(), "%d%m%Y_%H%M%S")
        log_file_path = "./Logs/testlog_" + cur_date + ".log"
        logger = logging.getLogger()
        file_handler = logging.FileHandler(log_file_path)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger
