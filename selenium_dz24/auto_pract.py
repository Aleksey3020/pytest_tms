from selenium_dz24.main_page import UtomationpracticeMain
from selenium_dz24.cart_page import UtomationpracticeCart
from selenium_dz24.login_page import UtomationpracticeLogin


def test_automationpractice(browser):
    main = UtomationpracticeMain(browser)
    main.open()
    main.check_for_expectation()
    main.woman_tab()

    # Переход с главной строницы на страницу корзина

    main.clicking_the_shopping_cart_button()
    cart = UtomationpracticeCart(browser)
    cart.checking_cart_for_expectation()
    cart.cart_is_empty()
    cart.exit_to_main_page()

    # Переход с главной строницы на страницу логина

    main.clicking_the_shopping_sign_in_button()
    sign_in = UtomationpracticeLogin(browser)
    sign_in.login_page_check()
    sign_in.visibility_already_registered()
    sign_in.create_an_account()
    sign_in.forgot_your_password()
    sign_in.exit_to_main_page()
