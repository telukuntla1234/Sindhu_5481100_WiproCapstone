from locators.hotel_locators import HotelLocators
from utils.logger import LogGen
from utils.waits import WaitUtils


logger = LogGen.loggen()


class HotelPage:
    def __init__(self, driver):
        self.driver = driver

    def select_destination(self, destination):
        box = WaitUtils.wait_for_element_clickable(self.driver, HotelLocators.DESTINATION_BOX)
        box.click()
        box.clear()
        box.send_keys(destination)
        WaitUtils.wait_for_element_clickable(
            self.driver,
            HotelLocators.DESTINATION_OPTION,
        ).click()
        logger.info(f"{destination} destination selected")

    def select_checkin(self):
        WaitUtils.wait_for_element_clickable(self.driver, HotelLocators.CHECKIN_BOX).click()
        logger.info("Check-in field selected")

    def select_checkin_date(self):
        WaitUtils.wait_for_element_clickable(self.driver, HotelLocators.CHECKIN_DATE).click()
        logger.info("Check-in date selected")

    def select_checkout_date(self):
        WaitUtils.wait_for_element_clickable(self.driver, HotelLocators.CHECKOUT_DATE).click()
        logger.info("Checkout date selected")

    def select_rooms(self):
        WaitUtils.wait_for_element_clickable(self.driver, HotelLocators.ROOM_GUESTS).click()
        logger.info("Rooms and guests selected")

    def click_search(self):
        WaitUtils.wait_for_element_clickable(self.driver, HotelLocators.SEARCH_BUTTON).click()
        logger.info("Search button clicked")
