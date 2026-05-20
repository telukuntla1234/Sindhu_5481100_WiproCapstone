from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.config_reader import ConfigReader
from utils.logger import LogGen


logger = LogGen.loggen()


class WaitUtils:
    @staticmethod
    def wait_for_element_visible(driver, locator, timeout=None):
        timeout = timeout or ConfigReader.get_timeout()
        try:
            logger.info(f"Waiting for element visible: {locator}")
            return WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            logger.error(f"Timeout waiting for visible element: {locator}")
            raise

    @staticmethod
    def wait_for_element_clickable(driver, locator, timeout=None):
        timeout = timeout or ConfigReader.get_timeout()
        try:
            logger.info(f"Waiting for element clickable: {locator}")
            return WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            logger.error(f"Timeout waiting for clickable element: {locator}")
            raise

    @staticmethod
    def wait_for_presence_of_element(driver, locator, timeout=None):
        timeout = timeout or ConfigReader.get_timeout()
        try:
            logger.info(f"Waiting for element present: {locator}")
            return WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            logger.error(f"Timeout waiting for present element: {locator}")
            raise

    @staticmethod
    def wait_for_url_contains(driver, text, timeout=None):
        timeout = timeout or ConfigReader.get_timeout()
        try:
            logger.info(f"Waiting for URL to contain: {text}")
            return WebDriverWait(driver, timeout).until(EC.url_contains(text))
        except TimeoutException:
            logger.error(f"Timeout waiting for URL to contain: {text}")
            raise

