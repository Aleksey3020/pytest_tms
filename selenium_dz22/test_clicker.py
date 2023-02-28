from selenium.webdriver.common.by import By


def test_clicker_xpath(browser):
    chrome = browser
    url = 'https://ultimateqa.com/complicated-page/'
    chrome.get(url=url)
    chrome.maximize_window()
    button = chrome.find_element(By.XPATH, '//a[@class="et_pb_button et_pb_button_4 et_pb_bg_layout_light"]')
    button.click()


def test_clicker_css(browser):
    chrome = browser
    url = 'https://ultimateqa.com/complicated-page/'
    chrome.get(url=url)
    chrome.maximize_window()
    button = chrome.find_element(By.CSS_SELECTOR, '.et_pb_button.et_pb_button_4.et_pb_bg_layout_light')
    button.click()


def test_clicker_class_name(browser):
    chrome = browser
    url = 'https://ultimateqa.com/complicated-page/'
    chrome.get(url=url)
    chrome.maximize_window()
    button = chrome.find_element(By.CLASS_NAME, "et_pb_button.et_pb_button_4.et_pb_bg_layout_light")
    button.click()


