import time

from selenium.webdriver.common.by import By

from driver.browser import chrome_driver
from page.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self):
        self.url = "http://192.168.1.42/Ecshop/user.php?act=register"
        # 元素定位符
        super().__init__()
        # self.driver = chrome_driver()
        self.locator_username = (By.NAME, 'username')  # 用户名输入框
        self.locator_email = (By.NAME, 'email')  # 邮件输入框
        self.locator_password = (By.NAME, 'password')  # 输入密码
        self.locator_confirm_password = (By.NAME, 'confirm_password') #确认密码
        self.locator_submit = (By.NAME, 'Submit')  # 注册按钮

        self.locator_assert = (By.XPATH,'//font[@id="ECS_MEMBERZONE"]/a[1]')

    def ele_username(self, username):  # 输入用户名
        self.driver.find_element(*self.locator_username).send_keys(username)

    def ele_email(self, email):  # 输入邮箱
        self.driver.find_element(*self.locator_email).send_keys(email)

    def ele_password(self, passwd):  # 输入密码
        self.driver.find_element(*self.locator_password).send_keys(passwd)

    def ele_confirm_password(self, confirm_password):  # 确认密码
        self.driver.find_element(*self.locator_confirm_password).send_keys(confirm_password)

    def ele_submit(self):  # 点击注册按钮
        self.driver.find_element(*self.locator_submit).click()

    def assert_register(self):
        result = self.driver.find_element(By.XPATH,'//font[@id="ECS_MEMBERZONE"]/a[1]').text
        return result

    def register(self, username,email,passwd,confirm_password):
        '''注册'''
        # self.driver.get(url=self.url)
        self.open(self.url)
        self.ele_username(username)
        self.ele_email(email)
        self.ele_password(passwd)
        self.ele_confirm_password(confirm_password)
        self.ele_submit()
        time.sleep(2)
        result = self.assert_result(self.locator_assert)

        self.quit()
        return result