import time

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from utils.logger import LogGen

logger = LogGen.loggen()


class PaymentPage:

    def __init__(self, driver):

        self.driver = driver

    PAYMENT_OPTION = (
        By.ID,
        "CARD"
    )
    CARD_NUMBER = (
        By.XPATH,
        "//input[@data-testid='card-number']"
    )

    EXPIRY_DATE = (
        By.XPATH,
        "//input[@data-testid='card-exp-date']"
    )

    CVV = (
        By.XPATH,
        "//input[@data-testid='new-card-cvv']"
    )

    SECURELY_PAY = (
        By.XPATH,
        "//button[contains(text(),'Securely Pay')]"
    )

    INVALID_CARD_ERROR = (
        By.XPATH,
        "//*[contains(text(),'valid card number')]"
    )

    def select_payment(self):

        time.sleep(5)

        payment = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(
                self.PAYMENT_OPTION
            )
        )

        payment.click()

    def enter_card_details(
            self,
            card_number,
            expiry,
            cvv
    ):
        card = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(
                self.CARD_NUMBER
            )
        )

        card.send_keys(card_number)

        logger.info("Card number entered")

        exp = self.driver.find_element(
            *self.EXPIRY_DATE
        )

        exp.send_keys(expiry)

        logger.info("Expiry date entered")

        cvv_field = self.driver.find_element(
            *self.CVV
        )

        cvv_field.send_keys(cvv)

        logger.info("CVV entered")

    def click_securely_pay(self):
        pay_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                self.SECURELY_PAY
            )
        )

        pay_btn.click()

        logger.info("Securely Pay button clicked")



    logger.info("Payment option selected successfully")