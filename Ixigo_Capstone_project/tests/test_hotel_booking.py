import time

import pytest

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

    def test_complete_booking(self, driver, data):

        logger.info("Opening IXIGO Website")

        home = HomePage(driver)

        hotel = HotelPage(driver)

        hotelselection = HotelSelection(driver)

        booking = BookingPage(driver)

        payment = PaymentPage(driver)

        # Handle popup
        home.handle_popup()

        ScreenshotUtil.capture_screenshot(
            driver,
            "homepage"
        )

        # Login
        home.click_login()

        logger.info("Login button clicked")

        home.enter_mobile_number(
            data["mobile"]
        )

        print("Enter OTP manually")

        time.sleep(15)

        print("Login completed manually")

        ScreenshotUtil.capture_screenshot(
            driver,
            "login_success"
        )

        # Open Hotels Section
        home.click_hotels()

        ScreenshotUtil.capture_screenshot(
            driver,
            "hotels_page"
        )

        # Destination
        hotel.select_destination(
            data["destination"]
        )

        # Check-in
        hotel.select_checkin()

        hotel.select_checkin_date()

        # Checkout
        # hotel.select_checkout()

        hotel.select_checkout_date()

        # Rooms and guests
        hotel.select_rooms()

        # Search hotels
        hotel.click_search()

        ScreenshotUtil.capture_screenshot(
            driver,
            "search_results"
        )

        # Close popup
        hotelselection.close_popup()

        # Filters
        time.sleep(3)

        hotelselection.free_breakfast()

        ScreenshotUtil.capture_screenshot(
            driver,
            "filters_applied"
        )

        # Book hotel
        hotelselection.click_book_now()

        ScreenshotUtil.capture_screenshot(
            driver,
            "booking_page"
        )

        booking.reserve_room()

        # Enter guest details
        booking.enter_guest_details(
            data["fname"],
            data["lname"],
            data["email"]
        )

        ScreenshotUtil.capture_screenshot(
            driver,
            "guest_details"
        )

        # Pay now
        booking.click_pay_now()

        # Payment page
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

        logger.info("Booking completed successfully")