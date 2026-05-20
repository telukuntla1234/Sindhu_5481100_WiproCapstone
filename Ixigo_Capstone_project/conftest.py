import os
import time

import pytest

from selenium import webdriver

from selenium.webdriver.edge.options import Options as EdgeOptions

from selenium.webdriver.chrome.options import Options as ChromeOptions

from utils.config_reader import ConfigReader

from utils.screenshot_util import ScreenshotUtil

from pages.homepage import HomePage


@pytest.fixture(scope="function")
def driver():

    browser = ConfigReader.get("browser")

    # CHROME
    if browser == "chrome":

        options = ChromeOptions()

        options.add_argument("--start-maximized")

        options.add_argument("--disable-notifications")

        driver = webdriver.Chrome(options=options)

    # EDGE
    else:

        options = EdgeOptions()

        options.add_argument("--start-maximized")

        options.add_argument("--disable-notifications")

        driver = webdriver.Edge(options=options)

    driver.get(
        ConfigReader.get("base_url")
    )

    yield driver

    driver.quit()


# ---------------------------------------------------
# LOGIN FIXTURE
# ---------------------------------------------------

@pytest.fixture(scope="function")

def logged_in_driver(driver):

    home = HomePage(driver)

    home.handle_popup()

    home.click_login()

    home.enter_mobile_number(
        "6301249799"
    )

    print("Enter OTP manually")

    time.sleep(15)

    print("Login successful")

    return driver


# ---------------------------------------------------
# SCREENSHOT ON FAILURE
# ---------------------------------------------------

@pytest.hookimpl(hookwrapper=True)

def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs["driver"]

        ScreenshotUtil.capture_screenshot(
            driver,
            "failed_test"
        )

# Allure test
def pytest_unconfigure(config):
    """
    This built-in Pytest hook runs exactly once after
    all tests have finished and the browsers are closed.
    """
    print("-------TESTS COMPLETE! GENERATING AND OPENING ALLURE REPORT--------")
    print("-------------------------------------------------------\n")

    # Automatically triggers the terminal command to open the report
    os.system("allure serve reports/allure-results")