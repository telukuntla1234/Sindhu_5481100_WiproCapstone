import os
import shutil
from datetime import datetime

from utils.logger import LogGen


logger = LogGen.loggen()

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
logger.info("========================================")
logger.info(f"IXIGO BDD AUTOMATION EXECUTION STARTED: {timestamp}")

if os.path.exists("reports/allure-results"):
    logger.info("Deleting old allure-results folder")
    shutil.rmtree("reports/allure-results")

if os.path.exists("reports/allure-report"):
    logger.info("Deleting old allure-report folder")
    shutil.rmtree("reports/allure-report")

logger.info("Starting Behave test execution")
behave_status = os.system("behave")
logger.info(f"Behave execution completed with status code: {behave_status}")

logger.info("Generating Allure HTML report")
allure_generate_status = os.system(
    "allure generate reports/allure-results -o reports/allure-report --clean"
)
logger.info(f"Allure report generated with status code: {allure_generate_status}")
logger.info("IXIGO BDD AUTOMATION EXECUTION COMPLETED")
logger.info("========================================")

