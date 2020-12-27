import time

from selenium.webdriver.common.by import By

from driver.browser import chrome_driver
from page.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self):
        self.url = "http://192.168.1.42/Ecshop/user.php"
        # 元素定位符
        # self.driver = chrome_driver()
        super().__init__()
        self.locator_username = (By.NAME, 'username')  # 用户名输入框
        self.locator_password = (By.NAME, 'password')  # 密码输入框
        self.locator_submit = (By.NAME, 'submit')  # 登录按钮
        self.locator_assert = (By.XPATH, '//font[@id="ECS_MEMBERZONE"]/a[1]')  #定位URL元素

    def ele_username(self, username):  # 用户名的定位及操作
        self.driver.find_element(*self.locator_username).send_keys(username)

    def ele_passwoed(self, passwd):  # 密码定位及操作
        self.driver.find_element(*self.locator_password).send_keys(passwd)

    def ele_submit(self):  # 登录按钮定位及操作
        self.driver.find_element(*self.locator_submit).click()

    def assert_result(self):
        '''断言处理'''
        actual_result = self.driver.find_element(*self.locator_assert).text
        return actual_result

    def login(self, username, passwd):
        '''登录逻辑'''
        self.driver.get(url=self.url)
        self.ele_username(username)
        self.ele_passwoed(passwd)
        self.ele_submit()
        time.sleep(2)

        actual_result = self.assert_result(self.locator_assert)

        self.driver.quit()

        return actual_result
