from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://192.168.1.42/Ecshop/user.php")
driver.find_element(By.NAME, "username").send_keys("luoliming")
driver.find_element(By.NAME, "password").send_keys("llm,1402726912")
driver.find_element(By.NAME, "submit").click()
driver.find_element(By.NAME,"keywords").send_keys("毛衣")
driver.find_element(By.NAME,"imageField").click()



time.sleep(3)
driver.quit()