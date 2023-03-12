@web_shop
Feature: Create an account
  I click on the button (create an account), an error appears

  Scenario: Error on an empty line
    Given open
    When click
    Then assert
