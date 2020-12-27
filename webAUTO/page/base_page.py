from driver.browser import chrome_driver

class BasePage():
    '''公共page'''
    def __init__(self):
        self.driver = chrome_driver()

    def assert_result(self,locator_assert):
        '''断言处理'''
        actual_result = self.driver.find_element(*locator_assert).text
        return actual_result

    def open(self):
        self.driver.get(url=self.url)
    def quit(self):
        self.driver.quit()