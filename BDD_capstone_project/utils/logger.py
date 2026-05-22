import logging
import os
from datetime import datetime


class LogGen:
    _logger = None
    _run_log_file = None
    _scenario_handler = None
    _scenario_log_file = None

    @staticmethod
    def loggen():
        if not os.path.exists("logs"):
            os.makedirs("logs")

        if LogGen._logger:
            return LogGen._logger

        logger = logging.getLogger("ixigo_bdd")
        logger.setLevel(logging.INFO)
        logger.propagate = False

        logger.handlers.clear()

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = f"logs/automation_{timestamp}.log"
        LogGen._run_log_file = log_file

        formatter = logging.Formatter(
            "%(asctime)s : %(levelname)s : %(message)s"
        )

        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        LogGen._logger = logger
        return logger

    @staticmethod
    def start_scenario_log(scenario_name):
        logger = LogGen.loggen()
        LogGen.stop_scenario_log()

        scenario_log_dir = "logs/scenarios"
        if not os.path.exists(scenario_log_dir):
            os.makedirs(scenario_log_dir)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        clean_name = LogGen._clean_file_name(scenario_name)
        scenario_log_file = f"{scenario_log_dir}/{clean_name}_{timestamp}.log"

        formatter = logging.Formatter(
            "%(asctime)s : %(levelname)s : %(message)s"
        )
        scenario_handler = logging.FileHandler(scenario_log_file, encoding="utf-8")
        scenario_handler.setFormatter(formatter)

        logger.addHandler(scenario_handler)
        LogGen._scenario_handler = scenario_handler
        LogGen._scenario_log_file = scenario_log_file
        return scenario_log_file

    @staticmethod
    def stop_scenario_log():
        if not LogGen._logger or not LogGen._scenario_handler:
            return

        LogGen._scenario_handler.flush()
        LogGen._logger.removeHandler(LogGen._scenario_handler)
        LogGen._scenario_handler.close()
        LogGen._scenario_handler = None
        LogGen._scenario_log_file = None

    @staticmethod
    def flush_handlers():
        logger = LogGen.loggen()
        for handler in logger.handlers:
            handler.flush()

    @staticmethod
    def get_scenario_log_file():
        return LogGen._scenario_log_file

    @staticmethod
    def get_run_log_file():
        return LogGen._run_log_file

    @staticmethod
    def _clean_file_name(value):
        return "".join(
            character if character.isalnum() or character in ("-", "_") else "_"
            for character in value
        )
