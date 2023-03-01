import time
from selenium.webdriver.common.by import By


def test1(browser):
    chrome = browser
    url = 'https://demoqa.com/text-box/'
    chrome.get(url=url)
    chrome.maximize_window()
    information = {'full_name': "Aleksey",
                   'mail': "adamkovich.leha@yandex.ru",
                   'cur_address': "Belarus, Baranovichi, st. Sovetskaya, 20",
                   'perm_address': "Belarus, Minsk, st. Lenina, 70"
                   }

    f_name = chrome.find_element(By.XPATH, '//*[@id="userName"]')
    f_name.send_keys(f"{information.get('full_name')}")
    email = chrome.find_element(By.ID, 'userEmail')
    email.send_keys(f"{information.get('mail')}")
    c_address = chrome.find_element(By.XPATH, '//*[@id="currentAddress"]')
    c_address.send_keys(f"{information.get('cur_address')}")
    p_address = chrome.find_element(By.ID, 'permanentAddress')
    p_address.send_keys(f"{information.get('perm_address')}")
    time.sleep(5)
    button_submit = chrome.find_element(By.ID, 'submit')
    button_submit.click()
    time.sleep(5)
    assert "Aleksey" == information.get('full_name')
    assert "adamkovich.leha@yandex.ru" == information.get('mail')
    assert "Belarus, Baranovichi, st. Sovetskaya, 20" == information.get('cur_address')
    assert "Belarus, Minsk, st. Lenina, 70" == information.get('perm_address')

