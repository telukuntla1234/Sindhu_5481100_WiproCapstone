import os

from datetime import datetime


class ScreenshotUtil:

    @staticmethod
    def capture_screenshot(driver, name):

        if not os.path.exists("screenshots"):

            os.makedirs("screenshots")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        path = f"screenshots/{name}_{timestamp}.png"

        driver.save_screenshot(path)

        print(f"Screenshot saved: {path}")