import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
class TestLogin(unittest.TestCase):

    def setUp(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("http://192.168.1.42/Ecshop/user.php")
        driver.find_element(By.NAME, "username").send_keys("luoliming")
        driver.find_element(By.NAME, "password").send_keys("llm,1402726912")
        driver.find_element(By.NAME, "submit").click()
        time.sleep(4)
        print("登录成功")
        driver.quit()
        ele = driver.current_url
        print(ele)
        expected = driver.current_url
        actual = driver.current_url

        self.assertEqual(expected, actual)

    def tearDown(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("http://192.168.1.42/Ecshop/user.php")
        driver.find_element(By.NAME, "username").send_keys("luoliming")
        driver.find_element(By.NAME, "password").send_keys("llm,1402726912")
        driver.find_element(By.NAME, "submit").click()

    def test_frist(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("http://192.168.1.42/Ecshop/user.php")
        driver.find_element(By.NAME, "username").send_keys("luoliming")
        driver.find_element(By.NAME, "password").send_keys("llm,1402726912")
        driver.find_element(By.NAME, "submit").click()
        driver.find_element(By.NAME, "keywords").send_keys("毛衣")
        driver.find_element(By.NAME, "imageField").click()
        print("搜索毛衣成功")

        time.sleep(3)
        driver.quit()


if __name__ == '__main__':
    # unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(TestLogin("test_frist"))
    runner = unittest.TextTestRunner()
    runner.run()
