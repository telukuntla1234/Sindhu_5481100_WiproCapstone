import logging
import os

from datetime import datetime


class LogGen:

    @staticmethod
    def loggen():

        if not os.path.exists("logs"):
            os.makedirs("logs")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        log_file = f"logs/automation_{timestamp}.log"

        logger = logging.getLogger()

        logger.setLevel(logging.INFO)

        if logger.hasHandlers():
            logger.handlers.clear()

        file_handler = logging.FileHandler(log_file)

        console_handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s : %(levelname)s : %(message)s"
        )

        file_handler.setFormatter(formatter)

        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        logger.addHandler(console_handler)

        return logger