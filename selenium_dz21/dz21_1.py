import time
from selenium.webdriver.common.by import By


def test2(browser):
    chrome = browser
    url = 'http://thedemosite.co.uk/savedata.php/'
    chrome.get(url=url)
    chrome.maximize_window()
    add_username = chrome.find_element(By.CSS_SELECTOR, '[tabindex="1"]')
    add_username.send_keys('rokki')
    add_password = chrome.find_element(By.NAME, 'password')
    add_password.send_keys('qwerrewq')
    button_save = chrome.find_element(By.NAME, 'FormsButton2')
    button_save.click()
    time.sleep(2)
