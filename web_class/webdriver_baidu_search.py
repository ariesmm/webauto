'''
#百度搜索
1.打开网页
2.找到输入框，输入关键字
3.点击【百度一下】搜索按钮
'''

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(1)
driver.get("http://www.baidu.com")

# driver.find_element_by_id("kw").send_keys("python") #找到输入框，输入关键词
# driver.find_element_by_name("wd").send_keys("selenium")#找到输入框，输入关键词
driver.find_element_by_class_name("s_ipt").send_keys("linux")  #找到输入框，输入关键词

driver.find_element_by_id("su").click()  #找到搜索按钮，点击
time.sleep(2)

# driver.find_element_by_link_text("linux_百度百科").click()  #点击‘linux_百度百科’进入页面
driver.find_element_by_partial_link_text("百度百科").click()  #点击‘百度百科’进入页面,模糊搜索

time.sleep(5)

driver.quit()
