from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

url = "http://192.168.1.42/Ecshop/user.php"
driver.get(url=url)

driver.find_element(By.NAME,'username').send_keys("luoliming")
driver.find_element(By.NAME,'password').send_keys("llm,1402726912")
driver.find_element(By.NAME,'submit').click()

time.sleep(2)
driver.quit()
