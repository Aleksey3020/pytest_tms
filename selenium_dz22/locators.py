from selenium.webdriver.common.by import By


def test_locator(browser):
    chrome = browser
    url = 'https://baraholka.onliner.by/'
    chrome.get(url=url)
    chrome.maximize_window()
    button = chrome.find_element(By.CSS_SELECTOR, '.b-btn-fleamarket__1>span')
    graphics_card = chrome.find_element(By.CSS_SELECTOR, '.b-cm-list>li:nth-child(9)>sup')
    print(graphics_card.text)
    dress = chrome.find_element(By.XPATH, '//div[@class="b-cm-col"][2]/div[@class="cm-onecat"][2]//li[5]/sup')
    print(dress.text)
