from behave import then, when

from pages.booking_page import BookingPage
from pages.hotel_page import HotelPage
from pages.hotel_selection_page import HotelSelection
from pages.payment_page import PaymentPage
from utils.logger import LogGen
from utils.screenshot_util import ScreenshotUtil
from utils.waits import WaitUtils


logger = LogGen.loggen()

# noinspection PyUnresolvedReferences
@when("User opens Hotels section")
def step_open_hotels(context):
    context.home_page.click_hotels()
    context.hotel_page = HotelPage(context.driver)
    ScreenshotUtil.capture_screenshot(context.driver, "hotels_page")


@when("User searches hotels with destination and dates from test data")
def step_search_hotels(context):
    data = context.test_data
    context.hotel_page.select_destination(data["destination"])
    context.hotel_page.select_checkin()
    context.hotel_page.select_checkin_date()
    context.hotel_page.select_checkout_date()
    context.hotel_page.select_rooms()
    context.hotel_page.click_search()
    ScreenshotUtil.capture_screenshot(context.driver, "hotel_search")


@when("User closes hotel results popup if present")
def step_close_results_popup(context):
    context.hotel_selection = HotelSelection(context.driver)
    context.hotel_selection.close_popup()


@when("User applies Free Breakfast filter")
def step_apply_free_breakfast(context):
    context.hotel_selection.free_breakfast()
    ScreenshotUtil.capture_screenshot(context.driver, "free_breakfast_filter")


@when("User selects the first available hotel")
def step_select_first_hotel(context):
    context.hotel_selection.click_book_now()
    context.booking_page = BookingPage(context.driver)
    ScreenshotUtil.capture_screenshot(context.driver, "booking_page")


@when("User reserves the recommended room")
def step_reserve_room(context):
    context.booking_page.reserve_room()


@when("User enters guest details from test data")
def step_enter_guest_details(context):
    data = context.test_data
    context.booking_page.enter_guest_details(
        data["fname"],
        data["lname"],
        data["email"],
    )
    ScreenshotUtil.capture_screenshot(context.driver, "guest_details")


@when("User enters empty guest details")
def step_enter_empty_guest_details(context):
    context.booking_page.enter_guest_details("", "", "")
    ScreenshotUtil.capture_screenshot(context.driver, "empty_guest_details")


@when("User proceeds to payment")
def step_proceed_payment(context):
    context.booking_page.click_pay_now()
    context.payment_page = PaymentPage(context.driver)


@when("User enters card details from test data")
def step_enter_card_details(context):
    data = context.test_data
    context.payment_page.select_payment()
    context.payment_page.enter_card_details(
        data["card"],
        data["expiry"],
        data["cvv"],
    )
    ScreenshotUtil.capture_screenshot(context.driver, "payment_card_details")


@when("User enters invalid card details")
def step_enter_invalid_card_details(context):
    context.payment_page.select_payment()
    context.payment_page.enter_card_details("42314562598", "12/30", "12")
    ScreenshotUtil.capture_screenshot(context.driver, "invalid_card_details")


@when("User clicks Securely Pay button")
def step_click_securely_pay(context):
    context.payment_page.click_securely_pay()



@then("Hotels search results should be displayed")
def step_verify_hotels_results(context):

    WaitUtils.wait_for_url_contains(context.driver, "hotels")

    current_url = context.driver.current_url.lower()

    assert "hotels" in current_url, \
        f"Hotel search results page not displayed. Current URL: {current_url}"

    ScreenshotUtil.capture_screenshot(context.driver, "search_results")


@then("Free Breakfast filter should be applied")
def step_verify_free_breakfast(context):

    current_url = context.driver.current_url.lower()

    assert "hotels" in current_url, \
        f"Hotel results page is not active after applying filter. Current URL: {current_url}"

    ScreenshotUtil.capture_screenshot(context.driver, "filters_applied")



@then("Guest details should be filled on booking page")
def step_verify_guest_details(context):

    values = context.booking_page.get_guest_field_values()

    assert values["first_name"] == context.test_data["fname"], \
        f"Expected first name {context.test_data['fname']} but got {values['first_name']}"

    assert values["last_name"] == context.test_data["lname"], \
        f"Expected last name {context.test_data['lname']} but got {values['last_name']}"

    assert values["email"] == context.test_data["email"], \
        f"Expected email {context.test_data['email']} but got {values['email']}"


@then("Payment card details should be accepted for validation")
def step_verify_payment_details(context):

    card_number = context.payment_page.get_card_number_value()

    assert card_number != "", \
        "Card number field is empty"

    assert len(card_number) >= 12, \
        f"Invalid card number entered: {card_number}"

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "payment_details_entered"
    )

@then("Invalid card number error should be displayed")
def step_verify_invalid_card_error(context):

    error_message = context.payment_page.get_invalid_card_error()

    assert error_message != "", \
        "No error message displayed for invalid card"

    assert "valid card number" in error_message.lower(), \
        f"Unexpected error message displayed: {error_message}"

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "invalid_card_validation"
    )

@then("Guest details fields should remain empty")
def step_verify_empty_guest_details(context):

    values = context.booking_page.get_guest_field_values()

    assert values["first_name"] == "", \
        f"Expected empty first name field but got: {values['first_name']}"

    assert values["last_name"] == "", \
        f"Expected empty last name field but got: {values['last_name']}"

    assert values["email"] == "", \
        f"Expected empty email field but got: {values['email']}"