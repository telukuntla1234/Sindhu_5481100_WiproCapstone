import time

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from utils.logger import LogGen

logger = LogGen.loggen()


class HotelSelection:

    def __init__(self, driver):

        self.driver = driver

    # Popup close button
    CLOSE_POPUP = (
        By.XPATH,
        "//div[@data-testid='bpg-home-modal-close']"
    )

    # FREE_CANCELLATION = (
    #     By.XPATH,
    #     "//p[text()='Free Cancellation']/ancestor::div[@role='listitem']"
    # )

    FREE_BREAKFAST = (
        By.XPATH,
        "//p[text()='Free Breakfast']/ancestor::div[@role='listitem']"
    )

    BOOK_NOW = (
        By.XPATH,
        "//button[contains(text(),'Book Now')][1]"
    )

    # Popup handler
    def close_popup(self):

        try:

            popup = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(
                    self.CLOSE_POPUP
                )
            )

            popup.click()

            logger.info("Hotel popup closed successfully")

        except:

            logger.warning("Hotel popup not displayed")


    # def free_cancellation(self):
    #
    #     self.driver.execute_script(
    #         "window.scrollBy(0, 500)"
    #     )
    #
    #     free = WebDriverWait(self.driver, 20).until(
    #         EC.element_to_be_clickable(
    #             self.FREE_CANCELLATION
    #         )
    #     )
    #
    #     free.click()
    #
    #     logger.info("Free cancellation filter selected")

    def free_breakfast(self):

        self.driver.execute_script(
            "window.scrollBy(0, 600)"
        )

        free_bf = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(
                self.FREE_BREAKFAST
            )
        )

        free_bf.click()

        logger.info("Free breakfast filter selected")

    def click_book_now(self):
        book_now = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                self.BOOK_NOW
            )
        )

        book_now.click()

        logger.info("Book now button clicked")



        self.driver.switch_to.window(
            self.driver.window_handles[-1]
        )

        logger.info("Switched to booking window")


