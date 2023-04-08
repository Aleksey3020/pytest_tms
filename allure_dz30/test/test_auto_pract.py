from allure_dz30.page.main_page import UtomationpracticeMain
from allure_dz30.page.cart_page import UtomationpracticeCart
from allure_dz30.page.login_page import UtomationpracticeLogin
import allure


@allure.feature('TEST1')
@allure.title('Website testing')
def test_automationpractice(browser):
    with allure.step('Open main page'):
        main = UtomationpracticeMain(browser)
        main.open()
    with allure.step('Сhecking if an element exists'):
        main.check_for_expectation()
    with allure.step('Presence of the element tab woman'):
        main.woman_tab()

    # Переход с главной строницы на страницу корзина
    with allure.step('Go to cart'):
        main.clicking_the_shopping_cart_button()
        cart = UtomationpracticeCart(browser)
    with allure.step('expected URL'):
        cart.checking_cart_for_expectation()
    with allure.step('Cart is empty'):
        cart.cart_is_empty()
    with allure.step('Go to main page'):
        cart.exit_to_main_page()

    # Переход с главной строницы на страницу логина
    with allure.step('Go to sign_in'):
        main.clicking_the_shopping_sign_in_button()
        sign_in = UtomationpracticeLogin(browser)
    with allure.step('Expected URL sign_in'):
        sign_in.login_page_check()
    with allure.step('Visibility of the opened page element'):
        sign_in.visibility_already_registered()
    with allure.step('Create_an_account'):
        sign_in.create_an_account()
    with allure.step('Forgot_your_password'):
        sign_in.forgot_your_password()
    with allure.step('Go to main page2'):
        sign_in.exit_to_main_page()
