from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from retrying import retry
import allure


class BasePage:
    def __init__(self, driver: webdriver.Chrome):
        self.webdriver = driver
        self.url: str = ''

    def open_url(self, url):
        self.webdriver.get(url)

    @allure.step('Go to page')
    def open(self):
        self.open_url(url=self.url)

    @allure.step('Find element')
    def find_element(self, locator: tuple, timer=10) -> WebElement:
        return WebDriverWait(self.webdriver, timer).until(EC.presence_of_element_located(locator))

    @allure.step('Click element')
    def click_element(self, locator: tuple, timer=10):
        return WebDriverWait(self.webdriver, timer).until(EC.element_to_be_clickable(locator)).click()

    @allure.step('Send keys')
    def send_keys(self, locator, content, timer=10):
        input_field = WebDriverWait(self.webdriver, timer).until(
            EC.element_to_be_clickable(locator))
        input_field.clear()
        input_field.send_keys(content)
