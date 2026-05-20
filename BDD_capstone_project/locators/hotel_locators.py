from selenium.webdriver.common.by import By


class HotelLocators:
    DESTINATION_BOX = (By.XPATH, "//input[@data-testid='location-input-web']")
    DESTINATION_OPTION = (By.XPATH, "(//div[@role='button'])[1]")
    CHECKIN_BOX = (By.XPATH, "//input[@data-testid='checkin-input']")
    CHECKIN_DATE = (
        By.XPATH,
        "//button[.//abbr[@aria-label='June 16, 2026']]",
    )
    CHECKOUT_DATE = (
        By.XPATH,
        "//button[.//abbr[@aria-label='June 18, 2026']]",
    )
    ROOM_GUESTS = (By.XPATH, "//input[@placeholder='Rooms & Guests']")
    SEARCH_BUTTON = (By.XPATH, "//button[@data-testid='search-hotels']")

