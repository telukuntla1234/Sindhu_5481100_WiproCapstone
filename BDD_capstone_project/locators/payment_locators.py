from selenium.webdriver.common.by import By


class PaymentLocators:
    PAYMENT_OPTION = (By.ID, "CARD")
    CARD_NUMBER = (By.XPATH, "//input[@data-testid='card-number']")
    EXPIRY_DATE = (By.XPATH, "//input[@data-testid='card-exp-date']")
    CVV = (By.XPATH, "//input[@data-testid='new-card-cvv']")
    SECURELY_PAY = (By.XPATH, "//button[contains(text(),'Securely Pay')]")
    INVALID_CARD_ERROR = (By.XPATH, "//*[contains(text(),'valid card number')]")

