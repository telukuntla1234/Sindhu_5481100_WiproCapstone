import logging
import os
from datetime import datetime


class LogGen:
    @staticmethod
    def loggen():
        if not os.path.exists("logs"):
            os.makedirs("logs")

        logger = logging.getLogger("ixigo_bdd")
        logger.setLevel(logging.INFO)
        logger.propagate = False

        if logger.handlers:
            return logger

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = f"logs/automation_{timestamp}.log"

        formatter = logging.Formatter(
            "%(asctime)s : %(levelname)s : %(message)s"
        )

        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        return logger

