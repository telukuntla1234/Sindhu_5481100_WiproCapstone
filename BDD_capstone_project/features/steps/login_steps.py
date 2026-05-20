from behave import given, then, when

from pages.home_page import HomePage
from utils.logger import LogGen
from utils.screenshot_util import ScreenshotUtil


logger = LogGen.loggen()

# noinspection PyUnresolvedReferences
@given("User launches Ixigo application")
def step_launch_ixigo(context):
    context.home_page = HomePage(context.driver)
    context.home_page.handle_popup()
    logger.info("Ixigo application launched")


@when("User clicks on Login button")
def step_click_login(context):
    context.home_page.click_login()


@when("User enters valid mobile number from test data")
def step_enter_valid_mobile(context):
    context.home_page.enter_mobile_number(context.test_data["mobile"])


@when('User enters invalid mobile number "{mobile}"')
def step_enter_invalid_mobile(context, mobile):
    context.home_page.enter_mobile_number(mobile)


@when("User clicks Continue button")
def step_click_continue(context):
    context.home_page.click_continue()


@when("User clicks Continue button if enabled")
def step_click_continue_if_enabled(context):
    try:
        context.home_page.click_continue()
    except Exception:
        logger.info("Continue button was not clickable for invalid mobile number")


@when("User submits valid mobile number for OTP")
def step_submit_mobile_for_otp(context):
    context.home_page.login_with_mobile_until_otp(context.test_data["mobile"])


@when("User enters OTP manually")
def step_manual_otp(context):
    context.home_page.wait_for_manual_otp_entry()
    ScreenshotUtil.capture_screenshot(context.driver, "manual_otp_entry")


@then("Login mobile number field should be displayed")
def step_verify_mobile_field(context):
    assert context.home_page.is_mobile_field_displayed(), "Login mobile number field is not displayed"
    ScreenshotUtil.capture_screenshot(context.driver, "login_mobile_field")


@then("OTP screen should be displayed")
def step_verify_otp_screen(context):
    assert context.home_page.wait_for_otp_screen(), "OTP screen was not displayed after mobile submission"
    ScreenshotUtil.capture_screenshot(context.driver, "otp_screen")


@then("Login flow should continue after manual OTP entry")
def step_verify_login_after_manual_otp(context):
    assert context.home_page.wait_for_login_overlay_to_close(), (
        "Login popup is still open. Please enter the OTP manually before the wait time ends."
    )
    assert context.driver.current_url.startswith("https://www.ixigo.com"), "Ixigo page is not active after OTP wait"
    ScreenshotUtil.capture_screenshot(context.driver, "login_after_manual_otp")


@then("User should remain on mobile number login screen or see mobile validation")
def step_verify_invalid_mobile_behavior(context):
    validation_message = context.home_page.get_mobile_validation_message()
    mobile_field_visible = context.home_page.is_mobile_field_displayed()
    assert validation_message or mobile_field_visible, "Invalid mobile validation was not visible"
    ScreenshotUtil.capture_screenshot(context.driver, "invalid_mobile_validation")
