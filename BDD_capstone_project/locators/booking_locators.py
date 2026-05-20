from selenium.webdriver.common.by import By


class BookingLocators:
    RESERVE_ROOM = (
        By.XPATH,
        "//button[@data-testid='reserve-recommended-room']",
    )
    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME = (By.NAME, "lastName")
    EMAIL = (By.NAME, "email")
    PAY_NOW = (By.XPATH, "//button[contains(text(),'Pay Now')]")

