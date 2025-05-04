import logging
import os
from datetime import datetime

class LoggerFactory:
    @staticmethod
    def get_logger(logger_name):
        current_date = datetime.now().strftime("%Y-%m-%d")
        logs_dir = "Reports\\Detailed_Logs\\"+current_date
        os.makedirs(logs_dir, exist_ok=True)
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        # Remove previous handlers if any (avoid duplication)
        if logger.hasHandlers():
            logger.handlers.clear()

        log_file = os.path.join(logs_dir, f"{logger_name}.log")
        fh = logging.FileHandler(log_file, mode='w')  # Overwrite on each run
        fh.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        logger.addHandler(fh)

        return logger
