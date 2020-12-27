from selenium import webdriver
'''封装浏览器驱动'''
def chrome_driver():
    '''Chrome浏览器'''
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)
    return driver


def firefox_driver():
    '''Firefox浏览器'''
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)
    return driver