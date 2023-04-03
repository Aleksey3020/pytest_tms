@web_shop
Feature: Create an account
  I click on the button (create an account), an error appears

  Scenario: Error on an empty line
    Given the Automation Practice main page is displayed
    When click sign in button
    Then error text: Invalid email address
