
from selenium import webdriver  # 引入webdriver

driver = webdriver.Chrome #启动Chrome浏览器，也是实例化Chrome

driver.get("http://www.baidu.com") #打开百度首页