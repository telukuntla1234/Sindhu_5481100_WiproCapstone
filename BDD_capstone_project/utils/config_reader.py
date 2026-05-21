import configparser

from utils.logger import LogGen


logger = LogGen.loggen()


class ConfigReader:
    config = configparser.ConfigParser()
    config.read("config/config.ini")

    @staticmethod
    def get(key):
        value = ConfigReader.config.get("DEFAULT", key)
        logger.info(f"Config fetched: {key}={value}")
        return value

    @staticmethod
    def get_base_url():
        return ConfigReader.get("base_url")

    @staticmethod
    def get_browser():
        return ConfigReader.get("browser")

    @staticmethod
    def get_timeout():
        return ConfigReader.config.getint("DEFAULT", "timeout")

    @staticmethod
    def get_implicit_wait():
        return ConfigReader.config.getint("DEFAULT", "implicit_wait")

    @staticmethod
    def get_headless():
        return ConfigReader.config.getboolean("DEFAULT", "headless")

    @staticmethod
    def get_manual_otp_wait():
        return ConfigReader.config.getint("DEFAULT", "manual_otp_wait")

    @staticmethod
    def get_auto_generate_allure():
        return ConfigReader.config.getboolean("DEFAULT", "auto_generate_allure")

    @staticmethod
    def get_auto_open_allure():
        return ConfigReader.config.getboolean("DEFAULT", "auto_open_allure")
