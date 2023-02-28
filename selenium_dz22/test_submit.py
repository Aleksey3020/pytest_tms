import time
from selenium.webdriver.common.by import By


def test1(browser):
    chrome = browser
    url = 'https://ultimateqa.com/filling-out-forms//'
    chrome.get(url=url)
    chrome.maximize_window()

    add_name = chrome.find_element(By.CSS_SELECTOR, '#et_pb_contact_name_0')
    add_name.send_keys('Aleksey')
    add_name1 = chrome.find_element(By.CSS_SELECTOR, '#et_pb_contact_name_1')
    add_name1.send_keys('Olga')

    add_message = chrome.find_element(By.CSS_SELECTOR, '#et_pb_contact_message_0')
    add_message.send_keys('Hello world')
    add_message1 = chrome.find_element(By.CSS_SELECTOR, '#et_pb_contact_message_1')
    add_message1.send_keys('Hello country')

    addition = chrome.find_element(By.XPATH, '//div[@class="et_pb_contact_right"]/p/input')
    addition.send_keys('13')

    time.sleep(5)
    submit = chrome.find_element(By.CSS_SELECTOR, '.et_contact_bottom_container>button')
    submit.click()
    submit1 = chrome.find_element(By.CSS_SELECTOR, '.et_pb_row.et_pb_row_1>div:nth-child(2)>div>div button')
    submit1.click()
    time.sleep(5)
    message = chrome.find_element(By.CSS_SELECTOR, '.et-pb-contact-message>p')
    message1 = chrome.find_element(By.CSS_SELECTOR, '.et_pb_row.et_pb_row_1>div:nth-child(2) p')
    assert 'Thanks for contacting us' == message.text
    assert 'Thanks for contacting us' == message1.text


def test2(browser):
    chrome = browser
    url = 'https://ultimateqa.com/filling-out-forms//'
    chrome.get(url=url)
    chrome.maximize_window()

    add_name = chrome.find_element(By.CSS_SELECTOR, '#et_pb_contact_name_0')
    add_name.send_keys('Aleksey')
    add_name1 = chrome.find_element(By.CSS_SELECTOR, '#et_pb_contact_name_1')
    add_name1.send_keys('Olga')

    addition = chrome.find_element(By.XPATH, '//div[@class="et_pb_contact_right"]/p/input')
    addition.send_keys('13')

    time.sleep(5)
    submit = chrome.find_element(By.CSS_SELECTOR, '.et_contact_bottom_container>button')
    submit.click()
    submit1 = chrome.find_element(By.CSS_SELECTOR, '.et_pb_row.et_pb_row_1>div:nth-child(2)>div>div button')
    submit1.click()
    time.sleep(5)
    message = chrome.find_element(By.CSS_SELECTOR, '.et-pb-contact-message>p')
    message1 = chrome.find_element(By.CSS_SELECTOR, '.et_pb_row.et_pb_row_1>div:nth-child(2) p')
    assert 'Please, fill in the following fields:' == message.text
    assert 'Please, fill in the following fields:' == message1.text


def test3(browser):
    chrome = browser
    url = 'https://ultimateqa.com/filling-out-forms//'
    chrome.get(url=url)
    chrome.maximize_window()

    add_message = chrome.find_element(By.CSS_SELECTOR, '#et_pb_contact_message_0')
    add_message.send_keys('Hello world')
    add_message1 = chrome.find_element(By.CSS_SELECTOR, '#et_pb_contact_message_1')
    add_message1.send_keys('Hello country')

    addition = chrome.find_element(By.XPATH, '//div[@class="et_pb_contact_right"]/p/input')
    addition.send_keys('13')

    time.sleep(5)
    submit = chrome.find_element(By.CSS_SELECTOR, '.et_contact_bottom_container>button')
    submit.click()
    submit1 = chrome.find_element(By.CSS_SELECTOR, '.et_pb_row.et_pb_row_1>div:nth-child(2)>div>div button')
    submit1.click()
    time.sleep(5)
    message = chrome.find_element(By.CSS_SELECTOR, '.et-pb-contact-message>p')
    message1 = chrome.find_element(By.CSS_SELECTOR, '.et_pb_row.et_pb_row_1>div:nth-child(2) p')
    assert 'Please, fill in the following fields:' == message.text
    assert 'Please, fill in the following fields:' == message1.text
