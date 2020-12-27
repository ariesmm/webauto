# 进入ECShop
# 点击注册
# 进行注册操作
#登录
from selenium import webdriver #引入webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()  #打开Chrome
driver.maximize_window()     #最大化窗口
driver.get("http://localhost/Ecshop/index.php")   #进入ECShop首页

driver.find_element(By.XPATH,'//font[@id="ECS_MEMBERZONE"]/a[2]').click() #点击进入注册页
driver.find_element(By.ID,"username").send_keys('luoluo') #输入用户名
driver.find_element(By.ID,"email").send_keys('12345556@qq.com')  #输入email
driver.find_element(By.ID,"password1").send_keys('123456')  #输入密码
driver.find_element(By.ID,"conform_password").send_keys('123456')   #二次确认密码
driver.find_element(By.XPATH,'/html/body/div[4]/div[3]/div[1]/form/table/tbody/tr[14]/td[2]/input[3]').click()  #点击注册
driver.find_element(By.XPATH,'/html/body/div[4]/div[3]/div[1]/div[1]/ul/li[1]/a').click() #点击用户登录

driver.find_element(By.NAME,"username").send_keys('luoluo') #输入用户名
driver.find_element(By.NAME,"password").send_keys('123456')  #输入密码

driver.find_element(By.NAME,"submit").click() #点击登录
time.sleep(4)
driver.quit()