Feature: Ixigo Hotel End To End Booking Functionality

  Background:
    Given User launches Ixigo application
    When User submits valid mobile number for OTP
    And User enters OTP manually
    Then Login flow should continue after manual OTP entry

  @hotel @e2e
  Scenario: Complete end to end hotel booking flow up to payment
    When User completes hotel search with Free Breakfast filter from test data
    And User completes hotel room booking with guest details from test data
    And User completes hotel payment details from test data
    Then End to end hotel booking flow should reach payment validation
