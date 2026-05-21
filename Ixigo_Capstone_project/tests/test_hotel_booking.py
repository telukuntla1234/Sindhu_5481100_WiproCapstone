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

        # -----------------------------
        # Homepage Validation
        # -----------------------------
        assert "ixigo" in driver.title.lower(), \
            "IXIGO homepage not loaded"

        # Handle popup
        home.handle_popup()

        ScreenshotUtil.capture_screenshot(
            driver,
            "homepage"
        )

        # -----------------------------
        # Login Section
        # -----------------------------
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

        # Assertion after login
        assert driver.current_url is not None, \
            "Login failed or page not loaded"

        # -----------------------------
        # Hotels Section
        # -----------------------------
        home.click_hotels()

        ScreenshotUtil.capture_screenshot(
            driver,
            "hotels_page"
        )

        # Assertion
        assert "hotel" in driver.current_url.lower() or \
               "hotel" in driver.page_source.lower(), \
            "Hotels page not opened"

        # -----------------------------
        # Destination Selection
        # -----------------------------
        hotel.select_destination(
            data["destination"]
        )

        # Assertion
        assert data["destination"].lower() in driver.page_source.lower(), \
            "Destination not selected properly"

        # -----------------------------
        # Check-in / Checkout
        # -----------------------------
        hotel.select_checkin()

        hotel.select_checkin_date()

        hotel.select_checkout_date()

        ScreenshotUtil.capture_screenshot(
            driver,
            "dates_selected"
        )

        # -----------------------------
        # Room Selection
        # -----------------------------
        hotel.select_rooms()

        # -----------------------------
        # Search Hotels
        # -----------------------------
        hotel.click_search()

        ScreenshotUtil.capture_screenshot(
            driver,
            "search_results"
        )

        # Assertion
        assert "hotel" in driver.page_source.lower(), \
            "Hotel search results not displayed"

        # -----------------------------
        # Close Popup
        # -----------------------------
        hotelselection.close_popup()

        # -----------------------------
        # Apply Filters
        # -----------------------------
        time.sleep(3)

        hotelselection.free_breakfast()

        ScreenshotUtil.capture_screenshot(
            driver,
            "filters_applied"
        )

        # Assertion
        assert "breakfast" in driver.page_source.lower(), \
            "Free breakfast filter not applied"

        # -----------------------------
        # Book Hotel
        # -----------------------------
        hotelselection.click_book_now()

        ScreenshotUtil.capture_screenshot(
            driver,
            "booking_page"
        )

        # Assertion
        assert "book" in driver.page_source.lower() or \
               "reserve" in driver.page_source.lower(), \
            "Booking page not opened"

        # -----------------------------
        # Reserve Room
        # -----------------------------
        booking.reserve_room()

        # -----------------------------
        # Guest Details
        # -----------------------------
        booking.enter_guest_details(
            data["fname"],
            data["lname"],
            data["email"]
        )

        ScreenshotUtil.capture_screenshot(
            driver,
            "guest_details"
        )

        # Assertion
        assert data["email"] in driver.page_source or \
               data["fname"] in driver.page_source, \
            "Guest details not entered properly"

        # -----------------------------
        # Payment Section
        # -----------------------------
        booking.click_pay_now()

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

        # Assertion
        assert "payment" in driver.page_source.lower() or \
               "card" in driver.page_source.lower(), \
            "Payment page not loaded"

        logger.info("Booking completed successfully")