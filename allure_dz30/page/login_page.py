import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from allure_dz30.page.base_page import BasePage


class LoginPageLocators:
    locator_alreade_registered = (By.CSS_SELECTOR, 'form[id="login_form"]')
    locator_exit = (By.CSS_SELECTOR, 'a[class="home"]')
    button_create_an_account = (By.CSS_SELECTOR, '[id="SubmitCreate"]>span')
    text_error = (By.CSS_SELECTOR, '[id="create_account_error"] li')
    password1 = (By.CSS_SELECTOR, '[class="lost_password form-group"]>a')
    string_input = (By.CSS_SELECTOR, '[class="form-control"]')
    retrieve_password = (By.CSS_SELECTOR, '[class="submit"]>button')
    text_error2 = (By.CSS_SELECTOR, '[class="alert alert-danger"] li')


class UtomationpracticeLogin(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'http://automationpractice.pl/index.php?controller=authentication&back=my-account'

    # Проверяем является ли данная страница ожидаемой
    @allure.step('Сhecking sign in for expectation')
    def login_page_check(self):
        assert self.url == self.webdriver.current_url

    # Проверяем, что мы на строницы логина
    @allure.step('Element on the sign in page')
    def visibility_already_registered(self):
        assert self.find_element(LoginPageLocators.locator_alreade_registered).is_displayed()

    # Проверяем, что Create an account кликабельная и после нажатия появляется ошибка: Invalid email address.

    @allure.step('Сlickability create_an_account')
    def create_an_account(self):
        pressing_a_button = self.click_element(LoginPageLocators.button_create_an_account)
        with allure.step('Wrong email input'):
            assert self.find_element(LoginPageLocators.text_error).text == 'Invalid email address.'
            allure.attach('Invalid email address.', name='error text')

    # Работаем с Forgot your password? Проверяем наличие ошибки при неправвильном вводе email

    @allure.step('Input email')
    def forgot_your_password(self):
        self.click_element(LoginPageLocators.password1)
        self.send_keys(LoginPageLocators.string_input, 'adamkovichyandex.ru')
        self.click_element(LoginPageLocators.retrieve_password)
        with allure.step('Email text error2'):
            assert self.find_element(LoginPageLocators.text_error2).text == 'Invalid email address.'
            allure.attach('Invalid email address.', name='error text')
    # Возвращаемся на главную страницу

    @allure.step('Exit_to_main_page')
    def exit_to_main_page(self):
        self.click_element(LoginPageLocators.locator_exit)
