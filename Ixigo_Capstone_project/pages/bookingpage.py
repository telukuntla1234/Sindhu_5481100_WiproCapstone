import time

from selenium.webdriver import Keys

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from utils.logger import LogGen

logger = LogGen.loggen()


class BookingPage:

    def __init__(self, driver):

        self.driver = driver

    RESERVE_ROOM = (
        By.XPATH,
        "//button[@data-testid='reserve-recommended-room']"
    )

    FIRST_NAME = (
        By.NAME,
        "firstName"
    )

    LAST_NAME = (
        By.NAME,
        "lastName"
    )

    EMAIL = (
        By.NAME,
        "email"
    )

    PAY_NOW = (
        By.XPATH,
        "//button[contains(text(),'Pay Now')]"
    )

    def reserve_room(self):

        reserve = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                self.RESERVE_ROOM
            )
        )

        reserve.click()

        logger.info("Reserve room button clicked")

    def enter_guest_details(self, fname, lname, email):

        first_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                self.FIRST_NAME
            )
        )

        first_name.send_keys(Keys.CONTROL + "a")

        first_name.send_keys(Keys.DELETE)

        first_name.send_keys(fname)

        last_name = self.driver.find_element(
            *self.LAST_NAME
        )

        last_name.send_keys(Keys.CONTROL + "a")

        last_name.send_keys(Keys.DELETE)

        last_name.send_keys(lname)

        email_field = self.driver.find_element(
            *self.EMAIL
        )

        email_field.send_keys(Keys.CONTROL + "a")

        email_field.send_keys(Keys.DELETE)

        email_field.send_keys(email)

        logger.info("Guest details entered successfully")

    def click_pay_now(self):

        pay = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                self.PAY_NOW
            )
        )

        pay.click()

        logger.info("Pay now button clicked")