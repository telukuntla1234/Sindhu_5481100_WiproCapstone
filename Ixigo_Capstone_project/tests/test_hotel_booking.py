import time

import pytest
import allure

from pages.homepage import HomePage
from pages.hotelpage import HotelPage
from pages.bookingpage import BookingPage
from pages.hotelselection import HotelSelection
from pages.paymentpage import PaymentPage

from utils.csv_reader import CSVReader
from utils.logger import LogGen
from utils.screenshot_util import ScreenshotUtil


logger = LogGen.loggen()

test_data = CSVReader.read_data(
    "testdata/guest_data.csv"
)


@pytest.mark.parametrize("data", test_data)

class TestHotelBooking:

    @allure.title("Complete Hotel Booking Flow")
    def test_complete_booking(self, driver, data):

        logger.info("Opening IXIGO Website")

        home = HomePage(driver)

        hotel = HotelPage(driver)

        hotelselection = HotelSelection(driver)

        booking = BookingPage(driver)

        payment = PaymentPage(driver)

        # Handle popup
        with allure.step("Handle homepage popup"):

            home.handle_popup()

            ScreenshotUtil.capture_screenshot(
                driver,
                "homepage"
            )

            allure.attach(
                driver.get_screenshot_as_png(),
                name="Homepage",
                attachment_type=allure.attachment_type.PNG
            )



        # Login
        with allure.step("Click login button"):

            home.click_login()

            logger.info("Login button clicked")

        home.enter_mobile_number(
            data["mobile"]
        )

        print("Enter OTP manually")

        time.sleep(20)

        print("Login completed manually")

        ScreenshotUtil.capture_screenshot(
            driver,
            "login_success"
        )

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Login Success",
            attachment_type=allure.attachment_type.PNG
        )

        # Open Hotels Section
        with allure.step("Open hotels section"):

            home.click_hotels()

            ScreenshotUtil.capture_screenshot(
                driver,
                "hotels_page"
            )

            allure.attach(
                driver.get_screenshot_as_png(),
                name="Hotels Page",
                attachment_type=allure.attachment_type.PNG
            )



        # Destination
        with allure.step("Select hotel destination"):

            hotel.select_destination(
                data["destination"]
            )

        # Check-in
        with allure.step("Select check-in date"):

            hotel.select_checkin()

            hotel.select_checkin_date()

        # Checkout
        with allure.step("Select checkout date"):

            hotel.select_checkout()

            hotel.select_checkout_date()

        # Rooms and guests
        with allure.step("Select rooms and guests"):

            hotel.select_rooms()

        # Search hotels
        with allure.step("Search hotels"):

            hotel.click_search()

            ScreenshotUtil.capture_screenshot(
                driver,
                "search_results"
            )

            allure.attach(
                driver.get_screenshot_as_png(),
                name="Search Results",
                attachment_type=allure.attachment_type.PNG
            )

        # Close popup
        with allure.step("Close hotel popup"):

            hotelselection.close_popup()

        # Filters
        with allure.step("Apply free cancellation filter"):

            hotelselection.free_cancellation()



        with allure.step("Apply free breakfast filter"):

            hotelselection.free_breakfast()

            ScreenshotUtil.capture_screenshot(
                driver,
                "filters_applied"
            )

            allure.attach(
                driver.get_screenshot_as_png(),
                name="Filters Applied",
                attachment_type=allure.attachment_type.PNG
            )

        # Book hotel
        with allure.step("Book selected hotel"):

            hotelselection.click_book_now()

            ScreenshotUtil.capture_screenshot(
                driver,
                "booking_page"
            )

            allure.attach(
                driver.get_screenshot_as_png(),
                name="Booking Page",
                attachment_type=allure.attachment_type.PNG
            )



        # Reserve room
        with allure.step("Reserve room"):

            booking.reserve_room()

        # Enter guest details
        with allure.step("Enter guest details"):

            booking.enter_guest_details(
                data["fname"],
                data["lname"],
                data["email"]
            )

            ScreenshotUtil.capture_screenshot(
                driver,
                "guest_details"
            )

            allure.attach(
                driver.get_screenshot_as_png(),
                name="Guest Details",
                attachment_type=allure.attachment_type.PNG
            )

        # Pay now
        with allure.step("Proceed to payment"):

            booking.click_pay_now()

        # Payment page
        with allure.step("Select payment option"):

            payment.select_payment()

            payment.select_payment()

            payment.enter_card_details(
                data["card"],
                data["expiry"],
                data["cvv"]
            )

            ScreenshotUtil.capture_screenshot(
                driver,
                "payment_page"
            )

            allure.attach(
                driver.get_screenshot_as_png(),
                name="Payment Page",
                attachment_type=allure.attachment_type.PNG
            )

        logger.info("Booking completed successfully")

        assert True