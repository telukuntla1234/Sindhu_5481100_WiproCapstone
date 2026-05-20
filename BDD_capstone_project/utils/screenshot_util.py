import os
from datetime import datetime

import allure

from utils.logger import LogGen


logger = LogGen.loggen()


class ScreenshotUtil:
    @staticmethod
    def capture_screenshot(driver, screenshot_name="screenshot"):
        screenshot_dir = "reports/screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        clean_name = screenshot_name.replace(" ", "_").replace("/", "_")
        screenshot_path = f"{screenshot_dir}/{clean_name}_{timestamp}.png"

        driver.save_screenshot(screenshot_path)
        logger.info(f"Screenshot saved at: {screenshot_path}")

        try:
            allure.attach.file(
                screenshot_path,
                name=clean_name,
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception as exc:
            logger.warning(f"Unable to attach screenshot to Allure: {exc}")

        return screenshot_path

