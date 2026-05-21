from behave import then, when

from pages.booking_page import BookingPage
from pages.hotel_page import HotelPage
from pages.hotel_selection_page import HotelSelection
from pages.payment_page import PaymentPage
from utils.screenshot_util import ScreenshotUtil


@when("User completes hotel search with Free Breakfast filter from test data")
def step_e2e_search_hotels_with_filter(context):
    data = context.test_data

    context.home_page.click_hotels()
    context.hotel_page = HotelPage(context.driver)
    ScreenshotUtil.capture_screenshot(context.driver, "e2e_hotels_page")

    context.hotel_page.select_destination(data["destination"])
    context.hotel_page.select_checkin()
    context.hotel_page.select_checkin_date()
    context.hotel_page.select_checkout_date()
    context.hotel_page.select_rooms()
    context.hotel_page.click_search()
    ScreenshotUtil.capture_screenshot(context.driver, "e2e_hotel_search")

    context.hotel_selection = HotelSelection(context.driver)
    context.hotel_selection.close_popup()
    context.hotel_selection.free_breakfast()
    ScreenshotUtil.capture_screenshot(context.driver, "e2e_free_breakfast_filter")


@when("User completes hotel room booking with guest details from test data")
def step_e2e_complete_room_booking(context):
    data = context.test_data

    context.hotel_selection.click_book_now()
    context.booking_page = BookingPage(context.driver)
    ScreenshotUtil.capture_screenshot(context.driver, "e2e_booking_page")

    context.booking_page.reserve_room()
    context.booking_page.enter_guest_details(
        data["fname"],
        data["lname"],
        data["email"],
    )
    ScreenshotUtil.capture_screenshot(context.driver, "e2e_guest_details")


@when("User completes hotel payment details from test data")
def step_e2e_complete_payment_details(context):
    data = context.test_data

    context.booking_page.click_pay_now()
    context.payment_page = PaymentPage(context.driver)
    context.payment_page.select_payment()
    context.payment_page.enter_card_details(
        data["card"],
        data["expiry"],
        data["cvv"],
    )
    ScreenshotUtil.capture_screenshot(context.driver, "e2e_payment_card_details")


@then("End to end hotel booking flow should reach payment validation")
def step_e2e_verify_payment_validation(context):

    card_number = context.payment_page.get_card_number_value()

    assert card_number != "", \
        "Payment card number field is empty"

    assert len(card_number) >= 12, \
        f"Invalid card number entered during end-to-end booking flow: {card_number}"

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "e2e_payment_details_entered"
    )