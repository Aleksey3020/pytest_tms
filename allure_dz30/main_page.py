from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium_dz24.base_page import BasePage
import allure

class MainPageLocators:
    visible_element_main_page = (By.CSS_SELECTOR, '[id = "slider_row"]')
    button_cart = (By.CSS_SELECTOR, '.shopping_cart>a')
    button_cart_sign_in = (By.CSS_SELECTOR, 'a[class="login"]')
    woman_tab_loc = (By.CSS_SELECTOR, '[title="Women"]')
    woman_tab_element = (By.CSS_SELECTOR, '[class="content_scene_cat"]')


class UtomationpracticeMain(BasePage):
    #@allure.step('input URL')
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'http://automationpractice.pl/index.php'

    # Провераем наличие элемента на главной страницы
    @allure.step('Element on the main page')
    def check_for_expectation(self):
        assert self.find_element(MainPageLocators.visible_element_main_page).is_displayed()

    # Кликаем на кнопку cart(корзина) и переходим в cart
    #@allure.step('Сlick cart button')
    def clicking_the_shopping_cart_button(self):
        self.click_element(MainPageLocators.button_cart)

    # Кликаем на кнопку sign in(логина) и переходим в sign in
    #@allure.step('Сlick sign in button')
    def clicking_the_shopping_sign_in_button(self):
        self.click_element(MainPageLocators.button_cart_sign_in)

    # Кликаем на вкладку woman и проверяем наличие элемента в вкладке
    @allure.step('Click woman tab')
    def woman_tab(self):
        self.click_element(MainPageLocators.woman_tab_loc)
        assert self.find_element(MainPageLocators.woman_tab_loc).is_displayed()
