from locators.payment_locators import PaymentLocators
from utils.logger import LogGen
from utils.waits import WaitUtils


logger = LogGen.loggen()


class PaymentPage:
    def __init__(self, driver):
        self.driver = driver

    def select_payment(self):
        WaitUtils.wait_for_element_clickable(self.driver, PaymentLocators.PAYMENT_OPTION).click()
        logger.info("Payment option selected successfully")

    def enter_card_details(self, card_number, expiry, cvv):
        WaitUtils.wait_for_element_clickable(
            self.driver,
            PaymentLocators.CARD_NUMBER,
        ).send_keys(card_number)
        self.driver.find_element(*PaymentLocators.EXPIRY_DATE).send_keys(expiry)
        self.driver.find_element(*PaymentLocators.CVV).send_keys(cvv)
        logger.info("Card details entered")

    def click_securely_pay(self):
        WaitUtils.wait_for_element_clickable(self.driver, PaymentLocators.SECURELY_PAY).click()
        logger.info("Securely Pay button clicked")

    def get_invalid_card_error(self):
        return WaitUtils.wait_for_element_visible(
            self.driver,
            PaymentLocators.INVALID_CARD_ERROR,
        ).text

    def get_card_number_value(self):
        return self.driver.find_element(*PaymentLocators.CARD_NUMBER).get_attribute("value")
