from selenium import webdriver  #应用webdriver
import time
from selenium. webdriver.common.by import By  #引入By类
driver = webdriver.Chrome() #启动浏览器
driver.maximize_window()
time.sleep(1)
driver.get("http://localhost/Ecshop/")
time.sleep(2)
driver.save_screenshot(".\ecshop.png") #截图保存到本地（返回图片文件）
time.sleep(2)
driver.find_element(By.LINK_TEXT,"收藏本站").click() #点击收藏出现，弹窗
time.sleep(2)
driver.switch_to.alert.accept()  #确认
time.sleep(2)
print(driver.title)
driver.quit()
