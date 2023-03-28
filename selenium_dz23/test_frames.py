import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test1(browser):
    chrome = browser
    url = 'http://the-internet.herokuapp.com/iframe'
    chrome.get(url=url)
    chrome.maximize_window()

    paragraph_t_locator = (By.CSS_SELECTOR, '.mce-content-body>p')
    iframe_locator = (By.CSS_SELECTOR, 'iframe[title="Rich Text Area"]')

    WebDriverWait(chrome, 10).until(EC.frame_to_be_available_and_switch_to_it(iframe_locator))
    paragraph_text = WebDriverWait(chrome, 10).until(EC.presence_of_element_located(paragraph_t_locator))

    assert 'Your content goes here.' == paragraph_text.text


