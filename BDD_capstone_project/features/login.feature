Feature: Ixigo Login Functionality

  Background:
    Given User launches Ixigo application

  @login @smoke
  Scenario: Open Ixigo login popup
    When User clicks on Login button
    Then Login mobile number field should be displayed

  @login
  Scenario: Enter valid mobile number and continue to OTP screen
    When User clicks on Login button
    And User enters valid mobile number from test data
    And User clicks Continue button
    Then OTP screen should be displayed

  @login @manual_otp
  Scenario: Complete login with manually entered OTP
    When User submits valid mobile number for OTP
    And User enters OTP manually
    Then Login flow should continue after manual OTP entry

  @login @negative
  Scenario: Validate invalid mobile number behavior
    When User clicks on Login button
    And User enters invalid mobile number "12345"
    And User clicks Continue button if enabled
    Then User should remain on mobile number login screen or see mobile validation

