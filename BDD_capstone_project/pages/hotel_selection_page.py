from locators.hotel_selection_locators import HotelSelectionLocators
from utils.logger import LogGen
from utils.waits import WaitUtils


logger = LogGen.loggen()


class HotelSelection:
    def __init__(self, driver):
        self.driver = driver

    def close_popup(self):
        try:
            WaitUtils.wait_for_element_clickable(
                self.driver,
                HotelSelectionLocators.CLOSE_POPUP,
                timeout=20,
            ).click()
            logger.info("Hotel popup closed successfully")
        except Exception:
            logger.warning("Hotel popup not displayed")

    def free_breakfast(self):
        self.driver.execute_script("window.scrollBy(0, 600)")
        WaitUtils.wait_for_element_clickable(
            self.driver,
            HotelSelectionLocators.FREE_BREAKFAST,
            timeout=20,
        ).click()
        logger.info("Free breakfast filter selected")

    def click_book_now(self):
        WaitUtils.wait_for_element_clickable(self.driver, HotelSelectionLocators.BOOK_NOW).click()
        logger.info("Book now button clicked")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        logger.info("Switched to booking window")
