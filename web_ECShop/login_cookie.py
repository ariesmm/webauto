from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://192.168.1.42/Ecshop/user.php")

driver.add_cookie({"name":"ECS[username]","value":"luoluo"})
driver.add_cookie({"name":"ECS[password]","value":"aed1b6309692d5606b7403db1a537a56"})
driver.add_cookie({"name":"ECS_ID","value":"c4cc07815d79f9d618879b2b2392014ac7fff4ff"})
driver.add_cookie({"name":"ECS[user_id]","value":"4"})
# driver.refresh()
driver.get("http://192.168.1.42/Ecshop/user.php")
time.sleep(3)
cookies = driver.get_cookies()
print(cookies)
time.sleep(2)
driver.quit()