from selenium.webdriver.common.by import By


class HomeLocators:
    POPUP_CLOSE = (By.XPATH, "//*[name()='svg' and @width='24']")
    LOGIN_BUTTON = (
        By.XPATH,
        "/html/body/main/div[1]/div/div[2]/div[2]/div/div/button",
    )
    MOBILE_NUMBER = (By.XPATH, "//input[@placeholder='Enter Mobile Number']")
    CONTINUE_BUTTON = (By.XPATH, "//button[contains(text(),'Continue')]")
    OTP_INPUT = (
        By.XPATH,
        "//input[contains(@placeholder,'OTP') or contains(@aria-label,'OTP') or @inputmode='numeric']",
    )
    LOGIN_ADVANTAGES_IMAGE = (
        By.XPATH,
        "//img[contains(@src,'login') and @alt='ixigo advantages']",
    )
    HOTELS_MENU = (By.XPATH, "(//a[contains(@href,'hotels')])[2]")
    MOBILE_ERROR = (
        By.XPATH,
        "//*[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'valid mobile') or "
        "contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'invalid mobile')]",
    )

