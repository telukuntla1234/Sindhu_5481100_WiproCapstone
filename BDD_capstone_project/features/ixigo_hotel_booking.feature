Feature: Ixigo Hotel Booking Functionality

  Background:
    Given User launches Ixigo application
    When User submits valid mobile number for OTP
    And User enters OTP manually
    Then Login flow should continue after manual OTP entry

  @hotel @search
  Scenario: Search hotels for destination from test data
    When User opens Hotels section
    And User searches hotels with destination and dates from test data
    Then Hotels search results should be displayed

  @hotel @filter
  Scenario: Apply Free Breakfast filter on hotel results
    When User opens Hotels section
    And User searches hotels with destination and dates from test data
    And User closes hotel results popup if present
    And User applies Free Breakfast filter
    Then Free Breakfast filter should be applied

  @hotel @booking
  Scenario: Enter guest details on booking page
    When User opens Hotels section
    And User searches hotels with destination and dates from test data
    And User closes hotel results popup if present
    And User selects the first available hotel
    And User reserves the recommended room
    And User enters guest details from test data
    Then Guest details should be filled on booking page

  @hotel @payment
  Scenario: Enter card details on payment page
    When User opens Hotels section
    And User searches hotels with destination and dates from test data
    And User closes hotel results popup if present
    And User selects the first available hotel
    And User reserves the recommended room
    And User enters guest details from test data
    And User proceeds to payment
    And User enters card details from test data
    Then Payment card details should be accepted for validation

  @hotel @payment @negative
  Scenario: Validate invalid card number error
    When User opens Hotels section
    And User searches hotels with destination and dates from test data
    And User closes hotel results popup if present
    And User selects the first available hotel
    And User reserves the recommended room
    And User enters guest details from test data
    And User proceeds to payment
    And User enters invalid card details
    And User clicks Securely Pay button
    Then Invalid card number error should be displayed

  @hotel @booking @negative
  Scenario: Validate empty guest details remain blank
    When User opens Hotels section
    And User searches hotels with destination and dates from test data
    And User closes hotel results popup if present
    And User selects the first available hotel
    And User reserves the recommended room
    And User enters empty guest details
    Then Guest details fields should remain empty

  @hotel @e2e
  Scenario: Complete end to end hotel booking flow up to payment
    When User opens Hotels section
    And User searches hotels with destination and dates from test data
    And User closes hotel results popup if present
    And User applies Free Breakfast filter
    And User selects the first available hotel
    And User reserves the recommended room
    And User enters guest details from test data
    And User proceeds to payment
    And User enters card details from test data
    Then Payment card details should be accepted for validation
