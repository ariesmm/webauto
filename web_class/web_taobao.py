from selenium import webdriver  #应用webdriver
import time

driver = webdriver.Chrome() #启动浏览器
driver.maximize_window()
time.sleep(1)
driver.get("http://www.taobao.com")  #进入淘宝
# time.sleep(3)
# driver.find_element_by_xpath('//input[@id="q"]').send_keys("凉鞋")#相对路径找搜索框
# time.sleep(2)
# driver.find_element_by_xpath('//form[@id="J_TSearchForm"]/div[1]/button').click()#复制xpath路径，*改成标签名
# time.sleep(2)
# driver.find_element_by_css_selector('.search-combobox-input').send_keys("CTR") #用css标签定位查找
#
# driver.find_element_by_css_selector('div[class="search-button"]>button').click() #用css标签定位搜索

driver.find_element_by_css_selector('div[]')
time.sleep(2)
driver.find_element_by_css_selector('')
driver.back()
time.sleep(3)
driver.quit()