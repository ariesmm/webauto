# 进入后台面
# 进入模板堂
# 选择模板
# 刷新页面
# 跳转前台首页
from selenium.webdriver.support.select import Select #引入类
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://localhost/Ecshop/admin/privilege.php?act=login")
driver.maximize_window()
driver.find_element(By.NAME, "username").send_keys('admin')  # 输入用户名
driver.find_element(By.NAME, "password").send_keys('llm,1402726912')  # 输入密码
driver.find_element(By.CLASS_NAME, "button").click()  # 点击按钮进入后台页面
# driver.find_element(By.CLASS_NAME,"collapse lis ico_10").click()  #点击“模板堂”

driver.switch_to.frame("menu-frame")  # 进入内嵌框（左边）
driver.find_element(By.XPATH, '//ul[@id="menu-ul"]/li[1]').click()  # 找到商品管理并点击
# driver.find_element(By.LINK_TEXT,"添加新商品").click()
driver.find_element(By.XPATH, '//ul[@id="menu-ul"]/li[1]/ul/li[2]/a').click()
time.sleep(2)  ###退出进入添加商品页面后，未等待时间，导致删除时间控件报错
driver.switch_to.parent_frame()  #退出frame
# driver.switch_to.default_content() #退到最外层
driver.switch_to.frame("main-frame")  # 进入中间页面
# 删除时间控件
js = "document.getElementById('promote_start_date').removeAttribute('readonly')"
# driver.execute_script(js)
driver.execute_script(js)

time.sleep(2)
driver.find_element(By.ID, "promote_start_date").clear()
driver.find_element(By.ID, "promote_start_date").send_keys("2020-02-03")  # 找到时间，修改时间
ele =driver.find_element(By.NAME,"goods_name_style")
# driver.find_element(By.NAME,"goods_name_style").click()
select = Select(ele)
# select.select_by_index(2)
select.select_by_value("strike")
# select.select_by_visible_text("加粗")
time.sleep(4)
driver.quit()
