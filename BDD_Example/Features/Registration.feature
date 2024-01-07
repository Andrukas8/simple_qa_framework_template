Feature: Verifying registration functionality

  @sanity @regression
  Scenario: Registration with valid data
    Given User is on registration page
    When  User enters username
    And User enters email id
    And User enters password
    And User clicks Signup button
    Then User should be registered successfully

  @sanity @smoke
  Scenario: Registration with duplicate user name data
    Given User is on Registration page again
    When User enters duplicate username
    And userAnd User enters email id
    And User enters password
    And User clicks Signup button
    Then User should not be registered
