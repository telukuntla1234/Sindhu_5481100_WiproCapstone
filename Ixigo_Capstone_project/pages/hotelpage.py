import time

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from utils.logger import LogGen

logger = LogGen.loggen()


class HotelPage:

    def __init__(self, driver):

        self.driver = driver

    DESTINATION_BOX = (
        By.XPATH,
        "//input[@data-testid='location-input-web']"
    )

    DESTINATION_OPTION = (
        By.XPATH,
        "(//div[@role='button'])[1]"
    )

    CHECKIN_BOX = (
        By.XPATH,
        "//input[@data-testid='checkin-input']"
    )

    CHECKIN_DATE = (
        By.XPATH,
        "//button[.//abbr[@aria-label='June 16, 2026']]"
    )
    #
    # CHECKOUT_BOX = (
    #     By.XPATH,
    #     "//input[@data-testid='checkout-input']"
    # )

    CHECKOUT_DATE = (
        By.XPATH,
        "//button[.//abbr[@aria-label='June 18, 2026']]"
    )

    ROOM_GUESTS = (
        By.XPATH,
        "//input[@placeholder='Rooms & Guests']"
    )

    ADULT_INCREMENT = (
        By.XPATH,
        "//p[@data-testid='-adult-increment']"
    )

    SEARCH_BUTTON = (
        By.XPATH,
        "//button[@data-testid='search-hotels']"
    )

    def select_destination(self, destination):

        box = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                self.DESTINATION_BOX
            )
        )

        box.click()

        box.send_keys(destination)

        option = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                self.DESTINATION_OPTION
            )
        )

        option.click()

        logger.info(f"{destination} destination selected")

    def select_checkin(self):

        chck_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                self.CHECKIN_BOX
            )
        )

        chck_btn.click()

        logger.info("Checkin selected")

    def select_checkin_date(self):

        chck_date = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                self.CHECKIN_DATE
            )
        )

        chck_date.click()

        logger.info("Checkin date selected")

    # def select_checkout(self):
    #
    #     chck_out = WebDriverWait(self.driver, 20).until(
    #         EC.element_to_be_clickable(
    #             self.CHECKOUT_BOX
    #         )
    #     )
    #
    #     chck_out.click()
    #
    #     logger.info("Checkout selected")

    def select_checkout_date(self):

        checkout_date = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                self.CHECKOUT_DATE
            )
        )

        checkout_date.click()

        logger.info("Checkout date selected")

    def select_rooms(self):

        room = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                self.ROOM_GUESTS
            )
        )

        room.click()

        logger.info("Rooms and guests selected")

    def select_adult_increment(self):

        adult = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                self.ADULT_INCREMENT
            )
        )

        adult.click()

        logger.info("Adult increment selected")

    def click_search(self):

        search_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                self.SEARCH_BUTTON
            )
        )

        search_btn.click()

        logger.info("Search button clicked")
