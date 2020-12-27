from selenium import webdriver  # 应用webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By  # 引入By类

driver = webdriver.Chrome()  # 启动浏览器
driver.maximize_window()
time.sleep(1)
driver.get("http://www.jd.com")  # 进入京东
# 鼠标悬浮停留在家用电器上
ele = driver.find_element(By.LINK_TEXT, "家用电器")
ac = ActionChains(driver)
ac.move_to_element(ele).perform()
time.sleep(4)
driver.find_element(By.XPATH, '//div[@id="cate_item1"]/div[1]/div[2]/dl[4]/dd/a[4]').click()
time.sleep(3)
handles = driver.window_handles
driver.switch_to.window(handles[1])
driver.find_element(By.ID, "key").send_keys(Keys.ENTER)
time.sleep(3)
# text = driver.find_element(By.XPATH, '//div[@id="J_goodsList"]/ul/li[2]/div/div[3]/a').text
text = driver.find_element(By.PARTIAL_LINK_TEXT,"静音节能").text
time.sleep(2)
print(text)
print(driver.title)
print(driver.current_url)

# driver.find_element(By.XPATH, '//div[@id="J_goodsList"]/ul/li[1]/div/div[1]/a/img').send_keys(Keys.ENTER)
time.sleep(3)
# ele = driver.find_element(By.CLASS_NAME,"cate_detail_con_lk")
# ac = ActionChains(driver)
# # ac.context_click(ele).perform()
# # ac.double_click(ele).perform()
# ac.click_and_hold(ele).perform()
# time.sleep(3)


# 点击家用电器
# driver.find_element(By.CLASS_NAME,"cate_menu_lk").click() #找到并点击
# size = driver.find_element(By.TAG_NAME,"html").size
# print("获取窗口大小",size)
#
# js = "window.scrollTo(500,1000)" #滚动屏幕取值（x,y）
# driver.execute_script(js)     #滚动屏幕
# time.sleep(3)
# driver.find_element(By.XPATH,'//div[@id="J_coupon"]/div[1]/a/h3').click()
# handles = driver.window_handles
# driver.switch_to.window(handles[1])
# driver.execute_script(js)
# time.sleep(3)
# driver.find_element(By.XPATH,'//div[@id="J_footer"]/div[2]/div/div/div[1]/ul/li[1]/a').click()
time.sleep(3)
driver.quit()
