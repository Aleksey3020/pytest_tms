from selenium_dz24.main_page import UtomationpracticeMain
from selenium_dz24.cart_page import UtomationpracticeCart
from selenium_dz24.login_page import UtomationpracticeLogin
from pytest_bdd import scenarios, given, when, then

scenarios('../selenium_dz25/web_shop.feature')


@given('the Automation Practice main page is displayed')
def open_automationpractice(browser):
    main = UtomationpracticeMain(browser)
    main.open()
    main.check_for_expectation()


@when('click sign in button')
def clicking_sign_in(browser):
    main = UtomationpracticeMain(browser)
    main.clicking_the_shopping_sign_in_button()


@then('error text: Invalid email address')
def assert_text_error(browser):
    sign_in = UtomationpracticeLogin(browser)
    sign_in.create_an_account()
