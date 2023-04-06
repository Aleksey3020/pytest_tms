from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium_dz24.base_page import BasePage


class CartPageLocators:
    locator_cart_is_empty = (By.CSS_SELECTOR, '.alert.alert-warning')
    locator_exit = (By.CSS_SELECTOR, 'a[class="home"]')


class UtomationpracticeCart(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'http://automationpractice.pl/index.php?controller=order'

    # Проверяем является ли данная страница ожидаемой

    def checking_cart_for_expectation(self):
        assert self.url == self.webdriver.current_url

    # Проверяем, что корзина пуста

    def cart_is_empty(self):
        assert self.find_element(CartPageLocators.locator_cart_is_empty).text == 'Your shopping cart is empty.'

    # Возвращаемся на главную страницу

    def exit_to_main_page(self):
        self.click_element(CartPageLocators.locator_exit)