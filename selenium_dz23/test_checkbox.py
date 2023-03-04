import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test1(browser):
    chrome = browser
    url = 'http://the-internet.herokuapp.com/dynamic_controls'
    chrome.get(url=url)
    chrome.maximize_window()

    checkbox_locator = (By.CSS_SELECTOR, '[id="checkbox"]')
    checkbox = WebDriverWait(chrome, 20).until(EC.presence_of_element_located(checkbox_locator))

    button_locator = (By.CSS_SELECTOR, 'button[type="button"]')
    button = WebDriverWait(chrome, 20).until(EC.element_to_be_clickable(button_locator))
    button.click()

    WebDriverWait(chrome, 10).until(EC.invisibility_of_element_located(checkbox))

    disable_locator = (By.XPATH, '//input[@type="text"]')
    disable = WebDriverWait(chrome, 10).until(EC.presence_of_element_located(disable_locator))

    assert not disable.is_enabled()

    button1_locator = (By.XPATH, '//form[@id="input-example"]/button')
    button1 = WebDriverWait(chrome, 20).until(EC.element_to_be_clickable(button1_locator))
    button1.click()

    enabled_locator = (By.CSS_SELECTOR, 'input[type="text"]')
    enable = WebDriverWait(chrome, 10).until(EC.presence_of_element_located(enabled_locator))
    time.sleep(5)

    assert enable.is_enabled()
