import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.feature('TEST3')
@allure.title('Iframe')
def test1(browser):
    with allure.step('Entrance'):
        chrome = browser
        url = 'http://the-internet.herokuapp.com/iframe'
        chrome.get(url=url)
    with allure.step('Maximize_window'):
        chrome.maximize_window()
    with allure.step('Lokators'):
        paragraph_t_locator = (By.CSS_SELECTOR, '.mce-content-body>p')
        iframe_locator = (By.CSS_SELECTOR, 'iframe[title="Rich Text Area"]')
    with allure.step('Open iframe'):
        WebDriverWait(chrome, 10).until(EC.frame_to_be_available_and_switch_to_it(iframe_locator))
    with allure.step('Element search'):
        paragraph_text = WebDriverWait(chrome, 10).until(EC.presence_of_element_located(paragraph_t_locator))
        with allure.step('Text in iframe'):
            assert 'Your content goes here.' == paragraph_text.text
            allure.attach(body=paragraph_text.text, name='Text')


