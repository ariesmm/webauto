# 登录，进入首页
# 搜索女装
# 选择第2个商品
# 清空购买数量，改为2
# 点击添加购物车
# 点击结算中心
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost/Ecshop/user.php")
driver.find_element(By.NAME,"username").send_keys('luoluo') #输入用户名
driver.find_element(By.NAME,"password").send_keys('123456')  #输入密码
driver.find_element(By.NAME,"submit").click() #点击登录
time.sleep(4)
driver.find_element(By.NAME,"keywords").send_keys("毛衣")  #在输入框，输入女装
driver.find_element(By.CLASS_NAME,"fm_hd_btm_shbx_bttn").click()  #点击搜索
driver.find_element(By.CLASS_NAME,"goodsimg").click() #点击进入第二个商品页面
driver.find_element(By.NAME,"number").clear()  #清除商品数量框商品数量
driver.find_element(By.ID,"number").send_keys("4")  #输入数量4
driver.find_element(By.XPATH,'//form[@id="ECS_FORMBUY"]/ul[3]/li[2]/a/img').click() #点击加入购物车
driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/table/tbody/tr/td[2]/a/img").click() #点击进入结算中心

time.sleep(6)
driver.quit()