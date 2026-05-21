from locators.home_locators import HomeLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.config_reader import ConfigReader
from utils.logger import LogGen
from utils.waits import WaitUtils


logger = LogGen.loggen()


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def handle_popup(self):
        try:
            popup = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(HomeLocators.POPUP_CLOSE)
            )
            self.driver.execute_script("arguments[0].click();", popup)
            logger.info("Popup closed successfully")
        except TimeoutException:
            logger.info("Popup not present")

        try:
            ActionChains(self.driver).move_by_offset(10, 10).click().perform()
        except Exception:
            logger.info("Page offset click skipped")

    def click_login(self):
        WaitUtils.wait_for_element_clickable(
            self.driver,
            HomeLocators.LOGIN_BUTTON,
        ).click()
        logger.info("Login button clicked")

    def enter_mobile_number(self, mobile):
        mobile_field = WaitUtils.wait_for_element_clickable(
            self.driver,
            HomeLocators.MOBILE_NUMBER,
        )
        mobile_field.clear()
        mobile_field.send_keys(mobile)
        logger.info("Mobile number entered")

    def click_continue(self):
        WaitUtils.wait_for_element_clickable(
            self.driver,
            HomeLocators.CONTINUE_BUTTON,
        ).click()
        logger.info("Continue button clicked")

    def login_with_mobile_until_otp(self, mobile):
        self.click_login()
        self.enter_mobile_number(mobile)
        self.click_continue()
        logger.info("Mobile submitted; waiting for OTP screen")

    def wait_for_otp_screen(self):
        try:
            WaitUtils.wait_for_presence_of_element(
                self.driver,
                HomeLocators.OTP_INPUT,
                timeout=10,
            )
            logger.info("OTP screen displayed")
            return True
        except TimeoutException:
            logger.info("OTP input was not detected; login popup may use segmented OTP fields")
            return self.is_mobile_field_displayed()

    def wait_for_manual_otp_entry(self):
        wait_time = ConfigReader.get_manual_otp_wait()
        print(f"Enter OTP manually within {wait_time} seconds")
        logger.info(f"Waiting up to {wait_time} seconds for manual OTP entry")
        try:
            WebDriverWait(self.driver, wait_time).until(
                lambda driver: not self.is_login_overlay_open()
            )
            logger.info("OTP accepted and login overlay closed")
            return True
        except TimeoutException:
            logger.error("OTP was not completed before wait time ended")
            return False

    def wait_for_login_overlay_to_close(self):
        try:
            WebDriverWait(self.driver, 3).until(
                lambda driver: not self.is_login_overlay_open()
            )
            logger.info("Login overlay closed after manual OTP entry")
            return True
        except TimeoutException:
            logger.error("Login overlay is still open after manual OTP wait")
            return False

    def is_login_overlay_open(self):
        login_elements = (
            self.driver.find_elements(*HomeLocators.MOBILE_NUMBER)
            + self.driver.find_elements(*HomeLocators.OTP_INPUT)
            + self.driver.find_elements(*HomeLocators.LOGIN_ADVANTAGES_IMAGE)
        )
        return any(element.is_displayed() for element in login_elements)

    def is_mobile_field_displayed(self):
        return len(self.driver.find_elements(*HomeLocators.MOBILE_NUMBER)) > 0

    def get_mobile_validation_message(self):
        messages = self.driver.find_elements(*HomeLocators.MOBILE_ERROR)
        if messages:
            return messages[0].text
        return ""

    def click_hotels(self):
        hotels = WaitUtils.wait_for_element_clickable(
            self.driver,
            HomeLocators.HOTELS_MENU,
        )
        self.driver.execute_script("arguments[0].click();", hotels)
        logger.info("Hotels menu clicked")
