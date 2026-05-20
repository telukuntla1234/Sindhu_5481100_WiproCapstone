from selenium.webdriver.common.by import By


class HotelSelectionLocators:
    CLOSE_POPUP = (By.XPATH, "//div[@data-testid='bpg-home-modal-close']")
    FREE_BREAKFAST = (
        By.XPATH,
        "//p[text()='Free Breakfast']/ancestor::div[@role='listitem']",
    )
    BOOK_NOW = (By.XPATH, "//button[contains(text(),'Book Now')][1]")

