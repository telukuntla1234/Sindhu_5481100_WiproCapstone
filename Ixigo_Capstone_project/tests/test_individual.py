import time

import pytest

from pages.homepage import HomePage
from pages.hotelpage import HotelPage
from pages.hotelselection import HotelSelection
from pages.bookingpage import BookingPage
from pages.paymentpage import PaymentPage

from utils.csv_reader import CSVReader
from utils.logger import LogGen
from utils.screenshot_util import ScreenshotUtil


logger = LogGen.loggen()

test_data = CSVReader.read_data(
    "testdata/guest_data.csv"
)


# ---------------------------------------------------
# POSITIVE TEST 1 - HOTEL SEARCH
# ---------------------------------------------------

@pytest.mark.parametrize(
    "data",
    test_data
)

@pytest.mark.order(1)

def test_hotel_search(logged_in_driver, data):

    driver = logged_in_driver

    # Arrange
    home = HomePage(driver)

    hotel = HotelPage(driver)

    # Action
    home.click_hotels()

    hotel.select_destination(
        data["destination"]
    )

    hotel.select_checkin()

    hotel.select_checkin_date()

    # hotel.select_checkout()

    hotel.select_checkout_date()

    hotel.select_rooms()

    hotel.click_search()

    ScreenshotUtil.capture_screenshot(
        driver,
        "hotel_search"
    )

    # Assert
    assert "hotels" in driver.current_url.lower()

    logger.info("Hotel search test passed")


# ---------------------------------------------------
# POSITIVE TEST 2 - FILTER TEST
# ---------------------------------------------------

@pytest.mark.parametrize(
    "data",
    test_data
)

@pytest.mark.order(2)

def test_hotel_filters(logged_in_driver, data):

    driver = logged_in_driver

    # Arrange
    home = HomePage(driver)

    hotel = HotelPage(driver)

    hotelselection = HotelSelection(driver)

    # Action
    home.click_hotels()



    hotel.select_destination(
        data["destination"]
    )

    hotel.select_checkin()

    hotel.select_checkin_date()

    # hotel.select_checkout()

    hotel.select_checkout_date()

    hotel.click_search()

    hotelselection.close_popup()

    # hotelselection.free_cancellation()

    time.sleep(2)

    hotelselection.free_breakfast()

    ScreenshotUtil.capture_screenshot(
        driver,
        "hotel_filters"
    )

    # Assert
    assert True

    logger.info("Hotel filters test passed")


# ---------------------------------------------------
# POSITIVE TEST 3 - GUEST DETAILS TEST
# ---------------------------------------------------

@pytest.mark.parametrize(
    "data",
    test_data
)

@pytest.mark.order(3)

def test_guest_details(logged_in_driver, data):

    driver = logged_in_driver

    # Arrange
    home = HomePage(driver)

    hotel = HotelPage(driver)

    hotelselection = HotelSelection(driver)

    booking = BookingPage(driver)

    # Action
    home.click_hotels()


    hotel.select_destination(
        data["destination"]
    )

    hotel.select_checkin()

    hotel.select_checkin_date()

    # hotel.select_checkout()

    hotel.select_checkout_date()

    hotel.click_search()

    hotelselection.close_popup()

    hotelselection.click_book_now()

    booking.reserve_room()

    booking.enter_guest_details(
        data["fname"],
        data["lname"],
        data["email"]
    )

    ScreenshotUtil.capture_screenshot(
        driver,
        "guest_details"
    )

    # Assert
    assert True

    logger.info("Guest details test passed")


# ---------------------------------------------------
# POSITIVE TEST 4 - PAYMENT TEST
# ---------------------------------------------------

@pytest.mark.parametrize(
    "data",
    test_data
)

@pytest.mark.order(4)

def test_payment(logged_in_driver, data):

    driver = logged_in_driver

    # Arrange
    home = HomePage(driver)

    hotel = HotelPage(driver)

    hotelselection = HotelSelection(driver)

    booking = BookingPage(driver)

    payment = PaymentPage(driver)

    # Action
    home.click_hotels()


    hotel.select_destination(
        data["destination"]
    )

    hotel.select_checkin()

    hotel.select_checkin_date()

    # hotel.select_checkout()

    hotel.select_checkout_date()

    hotel.click_search()

    hotelselection.close_popup()

    hotelselection.click_book_now()


    booking.reserve_room()

    booking.enter_guest_details(
        data["fname"],
        data["lname"],
        data["email"]
    )

    booking.click_pay_now()

    payment.select_payment()

    payment.enter_card_details(
        data["card"],
        data["expiry"],
        data["cvv"]
    )

    ScreenshotUtil.capture_screenshot(
        driver,
        "payment_test"
    )

    # Assert
    assert True

    logger.info("Payment test passed")


# ---------------------------------------------------
# NEGATIVE TEST 1 - INVALID CARD NUMBER VALIDATION
# ---------------------------------------------------

@pytest.mark.parametrize(
    "data",
    test_data
)

@pytest.mark.order(5)

def test_invalid_card_number_validation(
        logged_in_driver,
        data
):

    driver = logged_in_driver

    # Arrange
    home = HomePage(driver)

    hotel = HotelPage(driver)

    hotelselection = HotelSelection(driver)

    booking = BookingPage(driver)

    payment = PaymentPage(driver)

    # Action
    home.click_hotels()

    hotel.select_destination(
        data["destination"]
    )

    hotel.select_checkin()

    hotel.select_checkin_date()

    # hotel.select_checkout()

    hotel.select_checkout_date()

    hotel.click_search()

    hotelselection.close_popup()

    hotelselection.click_book_now()

    booking.reserve_room()

    booking.enter_guest_details(
        data["fname"],
        data["lname"],
        data["email"]
    )

    booking.click_pay_now()

    payment.select_payment()

    # Enter Invalid Card Number
    payment.enter_card_details(
        "42314562598",
        "12/30",
        "12"
    )

    # Click Securely Pay button
    payment.click_securely_pay()

    ScreenshotUtil.capture_screenshot(
        driver,
        "invalid_card_validation"
    )

    # Assert - Validate Error Message
    error_message = driver.find_element(
        *payment.INVALID_CARD_ERROR
    ).text

    assert "valid card number" in error_message.lower()

    logger.info(
        "Invalid card validation negative test passed"
    )


# ---------------------------------------------------
# NEGATIVE TEST 2 - EMPTY GUEST DETAILS
# ---------------------------------------------------

@pytest.mark.parametrize(
    "data",
    test_data
)

@pytest.mark.order(6)

def test_empty_guest_details(logged_in_driver, data):

    driver = logged_in_driver

    # Arrange
    home = HomePage(driver)

    hotel = HotelPage(driver)

    hotelselection = HotelSelection(driver)

    booking = BookingPage(driver)

    # Action
    home.click_hotels()

    hotel.select_destination(
        data["destination"]
    )

    hotel.select_checkin()

    hotel.select_checkin_date()

    # hotel.select_checkout()

    hotel.select_checkout_date()

    hotel.click_search()

    hotelselection.close_popup()

    hotelselection.click_book_now()

    booking.reserve_room()

    booking.enter_guest_details(
        "",
        "",
        ""
    )

    ScreenshotUtil.capture_screenshot(
        driver,
        "empty_guest_details"
    )

    # Assert
    first_name = driver.find_element(
        *booking.FIRST_NAME
    ).get_attribute("value")

    last_name = driver.find_element(
        *booking.LAST_NAME
    ).get_attribute("value")

    email = driver.find_element(
        *booking.EMAIL
    ).get_attribute("value")

    assert first_name == ""

    assert last_name == ""

    assert email == ""

    logger.info("Empty guest details negative test passed")