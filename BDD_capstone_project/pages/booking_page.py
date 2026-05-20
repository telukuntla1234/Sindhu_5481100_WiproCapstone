from locators.booking_locators import BookingLocators
from selenium.webdriver import Keys

from utils.logger import LogGen
from utils.waits import WaitUtils


logger = LogGen.loggen()


class BookingPage:
    def __init__(self, driver):
        self.driver = driver

    def reserve_room(self):
        WaitUtils.wait_for_presence_of_element(
            self.driver,
            BookingLocators.RESERVE_ROOM,
        ).click()
        logger.info("Reserve room button clicked")

    def enter_guest_details(self, fname, lname, email):
        first_name = WaitUtils.wait_for_presence_of_element(
            self.driver,
            BookingLocators.FIRST_NAME,
        )
        self._replace_value(first_name, fname)
        self._replace_value(self.driver.find_element(*BookingLocators.LAST_NAME), lname)
        self._replace_value(self.driver.find_element(*BookingLocators.EMAIL), email)
        logger.info("Guest details entered successfully")

    def click_pay_now(self):
        WaitUtils.wait_for_element_clickable(self.driver, BookingLocators.PAY_NOW).click()
        logger.info("Pay now button clicked")

    def get_guest_field_values(self):
        return {
            "first_name": self.driver.find_element(*BookingLocators.FIRST_NAME).get_attribute("value"),
            "last_name": self.driver.find_element(*BookingLocators.LAST_NAME).get_attribute("value"),
            "email": self.driver.find_element(*BookingLocators.EMAIL).get_attribute("value"),
        }

    @staticmethod
    def _replace_value(element, value):
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(value)
