'''
webdriver 控制浏览器
'''
from selenium import webdriver  # 引入webdriver
import time #等待时间（暂停一下）
driver = webdriver.Chrome()#启动Chrome浏览器，也是实例化Chrome

driver.maximize_window() #最大化浏览器窗口
driver.set_window_size(600,800) #设置窗口的大小
driver.get("http://www.baidu.com") #打开百度首页

time.sleep(2)  #等待2秒
driver.refresh() # 浏览器刷新

driver.get("http://www.taobao.com")  #打开淘宝

time.sleep(3)  #等待3秒
driver.get("http://www.jd.com")  #打开京东

time.sleep(3) #等待3秒
driver.back() #返回上一页面

time.sleep(3) #等待3秒
driver.forward() #前进到下一个页面

driver.quit() #退出所有窗口并关闭浏览器驱动（退出进程）
driver.close() #关闭浏览器（关闭窗口）（退出）