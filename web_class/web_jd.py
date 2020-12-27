from selenium import webdriver  #应用webdriver
import time
from selenium. webdriver.common.by import By  #引入By类
driver = webdriver.Chrome() #启动浏览器
driver.maximize_window()
time.sleep(1)
driver.get("http://www.jd.com")  #进入京东

driver.find_element(By.XPATH,'//input[@id="key"]').send_keys("手机")
#找到搜索框（用xpath），并输入关键字

time.sleep(2)
driver.find_element(By.XPATH,'//div[@id="search"]/div/div[2]/button').click() #找到搜索按钮（用xpath），并点击
time.sleep(2)
#点击进入第二个商品页面
driver.find_element(By.XPATH,'//div[@id="J_goodsList"]/ul/li[2]/div/div[1]/a/img').click()


handles = driver.window_handles  #获取页面句柄
print(handles)
driver.switch_to.window(handles[1]) #跳转第二个页面

price=driver.find_element(By.XPATH,'//span[@class="p-price"]/span[2]').text    #获取(打印）价格
print("价格",price)

driver.find_element(By.ID,"InitCartUrl").click() #找到【添加购物】，并点击添加购物车

handles = driver.window_handles  #获取页面句柄
print(handles)
driver.switch_to.window(handles[0]) #跳转第1个页面
driver.find_element(By.ID,'key').clear()  #清空搜索框
driver.find_element(By.ID,'key').send_keys("小米")  #输入小米
driver.find_element(By.CLASS_NAME,"iconfont").click() #找搜索，点击搜索
#点击进入第二个商品页面
driver.find_element(By.XPATH,'//div[@id="J_goodsList"]/ul/li[9]/div/div[1]/a/img').click()

time.sleep(3)
print(driver.title)

driver.quit()