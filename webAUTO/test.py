from selenium import webdriver  # 引入webdriver
import time

driver = webdriver.Chrome() #启动Chrome浏览器，也是实例化Chrome
driver.get("http://www.baidu.com") #打开百度首页

time.sleep(2)

driver.quit()
print("利用Jenkins进行新建项目，持续集成构建操作")