import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.feature('TEST2')
@allure.title('Dynamic Controls testing')
def test1(browser):
    # вход
    with allure.step('Entrance'):
        chrome = browser
        url = 'http://the-internet.herokuapp.com/dynamic_controls'
        chrome.get(url=url)

    # увеличение окна
    with allure.step('Maximize_window'):
        chrome.maximize_window()

    # Поиск элемента
    with allure.step('Element search'):
        checkbox_locator = (By.CSS_SELECTOR, '[id="checkbox"]')
        checkbox = WebDriverWait(chrome, 20).until(EC.presence_of_element_located(checkbox_locator))

    # элемент кликабельный
    with allure.step('Element clickability'):
        button_locator = (By.CSS_SELECTOR, 'button[type="button"]')
        button = WebDriverWait(chrome, 20).until(EC.element_to_be_clickable(button_locator))

    # Нажатие элемента
    with allure.step('Element click'):
        button.click()

    # Элемент не видимый
    with allure.step('Element invisibility'):
        button.click()
        WebDriverWait(chrome, 10).until(EC.invisibility_of_element_located(checkbox))

    # Поиск элемента2
    with allure.step('Element search 2'):
        disable_locator = (By.XPATH, '//input[@type="text"]')
        disable = WebDriverWait(chrome, 10).until(EC.presence_of_element_located(disable_locator))

    # Элемент isEnable или not isEnable
    with allure.step('Element isEnable or not isEnable'):
        assert not disable.is_enabled()
        allure.attach('False', name='result')

    # элемент кликабельный
    with allure.step('Element clickability 2'):
        button1_locator = (By.XPATH, '//form[@id="input-example"]/button')
        button1 = WebDriverWait(chrome, 20).until(EC.element_to_be_clickable(button1_locator))

    # Нажатие элемента
    with allure.step('Element click 2'):
        button1.click()

    # Поиск элемента3
    with allure.step('Element search 3'):
        enabled_locator = (By.CSS_SELECTOR, 'input[type="text"]')
        enable = WebDriverWait(chrome, 10).until(EC.presence_of_element_located(enabled_locator))
        time.sleep(5)

    # Элемент isEnable или not isEnable
    with allure.step('Element isEnable or not isEnable 2'):
        assert enable.is_enabled()
        allure.attach('True', name='result')
