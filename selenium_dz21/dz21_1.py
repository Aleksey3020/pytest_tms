import time
from selenium.webdriver.common.by import By


def test2(browser):
    chrome = browser
    url = 'http://thedemosite.co.uk/savedata.php/'
    chrome.get(url=url)
    chrome.maximize_window()
    add_username = chrome.find_element(By.NAME, 'username')
    add_username.send_keys('fdgghgfhgf')
    add_password = chrome.find_element(By.NAME, 'password')
    add_password.send_keys('dfgdfg')
    button_save = chrome.find_element(By.NAME, 'FormsButton2')
    button_save.click()


