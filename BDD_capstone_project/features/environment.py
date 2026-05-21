import os
import shutil
import subprocess

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from utils.config_reader import ConfigReader
from utils.csv_reader import CSVReader
from utils.logger import LogGen
from utils.screenshot_util import ScreenshotUtil


logger = LogGen.loggen()


def before_all(context):
    context.test_data = CSVReader.first_row("testdata/guest_data.csv")


def before_scenario(context, scenario):
    logger.info("========================================")
    logger.info(f"STARTING SCENARIO: {scenario.name}")

    browser = ConfigReader.get_browser().lower()
    headless = ConfigReader.get_headless()

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        if headless:
            options.add_argument("--headless=new")
        context.driver = webdriver.Chrome(options=options)
    else:
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        if headless:
            options.add_argument("--headless=new")
        context.driver = webdriver.Edge(options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(ConfigReader.get_implicit_wait())
    context.driver.get(ConfigReader.get_base_url())
    logger.info("Browser opened and Ixigo URL loaded")


def after_scenario(context, scenario):
    logger.info(f"Scenario status: {scenario.status}")
    status_name = getattr(scenario.status, "name", str(scenario.status)).lower()
    if status_name in ("failed", "error"):
        screenshot_path = ScreenshotUtil.capture_screenshot(
            context.driver,
            scenario.name,
        )
        logger.error(f"Scenario did not pass. Screenshot saved: {screenshot_path}")
    else:
        logger.info(f"Scenario passed: {scenario.name}")

    context.driver.quit()
    logger.info("Browser closed successfully")
    logger.info("========================================")


def after_all(context):
    if not ConfigReader.get_auto_generate_allure():
        return

    allure_command = shutil.which("allure")
    if not allure_command:
        logger.warning("Allure command not found. Install Allure CLI to generate HTML reports automatically.")
        return

    logger.info("Tests completed. Generating Allure report.")
    os.makedirs("reports/allure-report", exist_ok=True)
    generate_result = subprocess.run(
        [
            allure_command,
            "generate",
            "reports/allure-results",
            "-o",
            "reports/allure-report",
            "--clean",
        ],
        shell=False,
        check=False,
    )

    if generate_result.returncode != 0:
        logger.error("Allure report generation failed.")
        return

    logger.info("Allure report generated successfully.")

    if ConfigReader.get_auto_open_allure():
        logger.info("Opening Allure report.")
        subprocess.Popen(
            [allure_command, "open", "reports/allure-report"],
            shell=False,
        )
