import time

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

from utils.logger import LogGen

logger = LogGen.loggen()


class HomePage:

    def __init__(self, driver):

        self.driver = driver

    POPUP_CLOSE = (
        By.XPATH,
        "//*[name()='svg' and @width='24']"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "/html/body/main/div[1]/div/div[2]/div[2]/div/div/button"
    )

    MOBILE_NUMBER =(
        By.XPATH,
        "//input[@placeholder='Enter Mobile Number']"
    )

    CONTINUE_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Continue')]"
    )


    HOTELS_MENU = (
        By.XPATH,
        "(//a[contains(@href,'hotels')])[2]"
    )

    def handle_popup(self):

        try:

            popup = WebDriverWait(self.driver, 8).until(
                EC.presence_of_element_located(
                    self.POPUP_CLOSE
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                popup
            )

            logger.info("Popup closed successfully")

        except Exception:

            logger.info("Popup not present")

        ActionChains(self.driver).move_by_offset(
            10,
            10
        ).click().perform()

    def click_login(self):

        login_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                self.LOGIN_BUTTON
            )
        )

        login_btn.click()

        logger.info("Login button clicked")

    def enter_mobile_number(self, mobile):

        mobile_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                self.MOBILE_NUMBER
            )
        )

        mobile_field.send_keys(mobile)

        logger.info("Mobile number entered")

        continue_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                self.CONTINUE_BUTTON
            )
        )

        continue_btn.click()

        logger.info("Continue button clicked")

    def click_hotels(self):

        hotels = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                self.HOTELS_MENU
            )
        )

        hotels.click()

        logger.info("Hotels menu clicked")