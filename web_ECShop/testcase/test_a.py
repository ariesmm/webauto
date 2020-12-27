import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
class TestLogin(unittest.TestCase):

    def setUp(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("http://192.168.1.42/Ecshop/user.php")
        driver.find_element(By.NAME, "username").send_keys("luoliming")
        driver.find_element(By.NAME, "password").send_keys("llm,1402726912")
        driver.find_element(By.NAME, "submit").click()
        time.sleep(4)
        print("登录成功")
        driver.quit()
        self.assertEqual(True, True)

    def tearDown(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("http://192.168.1.42/Ecshop/user.php")
        driver.find_element(By.NAME, "username").send_keys("luoliming")
        driver.find_element(By.NAME, "password").send_keys("llm,1402726912")
        driver.find_element(By.NAME, "submit").click()


    def test_frist(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("http://192.168.1.42/Ecshop/user.php")
        driver.find_element(By.NAME, "username").send_keys("luoliming")
        driver.find_element(By.NAME, "password").send_keys("llm,1402726912")
        driver.find_element(By.NAME, "submit").click()
        driver.find_element(By.NAME, "keywords").send_keys("毛衣")
        driver.find_element(By.NAME, "imageField").click()
        print("搜索毛衣成功")

        time.sleep(3)
        driver.quit()

    def test_second(self):
        '''
        登录后台
        进入订单管理
        进入订单列表
        对订单列表进行搜索、查询、删除、打印
        '''
        from selenium import webdriver  # 引入webdriver
        import time  # 引入时间
        from selenium.webdriver.common.by import By  # 引入By类
        from selenium.webdriver.common.action_chains import ActionChains  # 引入ActionChains类
        from selenium.webdriver.common.keys import Keys  # 引入keys
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://192.168.1.120/upload/admin")
        # 登录后台账户和密码
        driver.find_element(By.NAME, "username").send_keys("admin")
        driver.find_element(By.NAME, "password").send_keys("banxian123")
        driver.find_element(By.CLASS_NAME, "button").click()
        # 进入左边内联框架
        driver.switch_to.frame("menu-frame")
        # 点击订单管理
        driver.find_element(By.XPATH, '//ul[@id="menu-ul"]/li[3]').click()
        # 点击订单列表
        driver.find_element(By.XPATH, '//ul[@id="menu-ul"]/li[3]/ul/li[1]/a').click()
        driver.switch_to.parent_frame()  # 退回到上一层frame
        time.sleep(2)
        driver.switch_to.frame("main-frame")  # 进入到main—frame
        # 实现鼠标悬浮
        ele = driver.find_element(By.XPATH, '//a[@id="order_0"]')
        action = ActionChains(driver)
        action.move_to_element(ele).perform()
        # 从悬浮图片上进入商品详情
        driver.find_element(By.XPATH, '//div[@id="order_goods_layer"]/table/tbody/tr[2]/td[1]/a').click()
        time.sleep(2)
        # 页面切换
        handles = driver.window_handles
        driver.switch_to.window(handles[0])
        driver.switch_to.frame("main-frame")  # 进入main-frame页面
        # 点击订单号，进入订单详情页面
        driver.find_element(By.XPATH, '//a[@id="order_0"]').click()
        # 点击进入上一个订单
        driver.find_element(By.XPATH, '//form[@name="theForm"]/div[1]/table/tbody/tr[1]/td/div/input[1]').click()
        # 点击进入下一个订单
        driver.find_element(By.CSS_SELECTOR, "input[name='next']").click()
        # 点击打印订单
        driver.find_element(By.CSS_SELECTOR, 'input[value="打印订单"]').click()
        # 返回上一页面
        driver.switch_to.window(handles[0])
        driver.switch_to.frame("main-frame")
        # 点击订单列表
        driver.find_element(By.XPATH, '//span[@class="action-span"]/a').click()
        # 鼠标返回
        driver.back()
        # 显示购物者信息
        # driver.find_element(By.XPATH,'//form[@name="theForm"]/div[1]/table/tbody/tr[4]/td[2]/a[1]').click()
        # 点击支付方式编辑
        driver.switch_to.frame("main-frame")
        driver.find_element(By.XPATH, '//form[@name="theForm"]/div[1]/table/tbody/tr[5]/td[2]/a').click()
        # 选择支付方式
        driver.find_element(By.XPATH, '//div[@class="list-div"]/table/tbody/tr[3]/td[1]/input').click()
        driver.find_element(By.CLASS_NAME, "button").click()  # 确定
        # 点击配送方式编辑
        driver.find_element(By.XPATH, '//div[@class="list-div"]/table/tbody/tr[6]/td[2]/a').click()
        # 选择配送方式
        driver.find_element(By.XPATH, '//div[@class="list-div"]/table/tbody/tr[3]/td[1]/input').click()
        # 选择我要报价
        driver.find_element(By.NAME, "insure").click()
        # 确定
        driver.find_element(By.NAME, "finish").click()
        # 配送方式，打印快递单
        driver.find_element(By.XPATH, '//div[@class="list-div"]/table/tbody/tr[6]/td[2]/input').click()
        # 切回main-frame页面
        driver.switch_to.window(handles[0])
        driver.switch_to.frame("main-frame")
        driver.find_element(By.XPATH, '//div[@class="list-div"]/table/tbody/tr[8]/th/a').click()
        # 点击确定
        driver.find_element(By.NAME, "finish").click()
        # 退到最外层
        driver.switch_to.default_content()
        # 进到header-frame
        driver.switch_to.frame("header-frame")
        # 点击退出
        driver.find_element(By.XPATH, '//div[@id="submenu-div"]/ul/li[1]/a/span').click()

        time.sleep(3)
        driver.quit()

    def test_third(self):
        '''
        ECShop注册功能：
        进入网页
        找到【注册】
        点击进入【注册】
        注册输入框，输入数据，进行注册
        注册成功，跳转页面
        '''
        from selenium import webdriver
        import time
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.select import Select
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        driver.get("http://192.168.1.120/upload/")
        driver.maximize_window()
        driver.find_element(By.XPATH, '//font[@id="ECS_MEMBERZONE"]/a[2]').click()
        driver.find_element(By.ID, "username").send_keys("mingming")
        driver.find_element(By.ID, "email").send_keys("1336666@qq.com")
        driver.find_element(By.ID, "password1").send_keys("123456")
        driver.find_element(By.ID, "conform_password").send_keys("123456")
        driver.find_element(By.NAME, "extend_field5").click()
        driver.find_element(By.NAME, "extend_field5").send_keys("13112341234")

        ele = driver.find_element(By.NAME, "sel_question")
        select = Select(ele)
        select.select_by_value("friend_birthday")
        driver.find_element(By.NAME, "passwd_answer").send_keys("321")

        driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[1]/form/table/tbody/tr[9]/td[2]/label/a').click()
        time.sleep(2)
        handles = driver.window_handles
        driver.switch_to.window(handles[0])
        driver.find_element(By.NAME, "agreement").click()
        time.sleep(2)
        driver.find_element(By.NAME, "agreement").click()
        time.sleep(2)
        driver.find_element(By.NAME, "Submit").click()
        time.sleep(4)

        driver.quit()

    def test_forth(self):
        '''
        用户登录后，在首页进行商品选购
        添加购物车
        提交订单
        产看订单
        对订单进行合并，确认和取消
        '''
        from typing import Any, Union

        from selenium import webdriver
        import time
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.select import Select

        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://192.168.1.120/upload/")
        driver.find_element(By.XPATH, '//font[@id="ECS_MEMBERZONE"]/a[1]').click()  # 进入登录
        driver.find_element(By.NAME, "username").send_keys("mingming")  # 输入用户名
        driver.find_element(By.NAME, "password").send_keys("123456")  # 输入密码
        driver.find_element(By.NAME, "remember").click()  # 勾选记住信息
        driver.find_element(By.NAME, "submit").click()  # 点击登录
        time.sleep(4)
        driver.find_element(By.ID, "keyword").send_keys("毛衣")  # 找到搜索框，搜索毛衣
        driver.find_element(By.NAME, "imageField").click()  # 点击搜索
        # 找到第2个商品，点击进入商品详情页
        driver.find_element(By.XPATH, '//form[@id="compareForm"]/div/div[2]/a/img').click()
        # 清空默认商品数量
        driver.find_element(By.NAME, "number").clear()
        # 更改商品数量
        driver.find_element(By.NAME, "number").send_keys("4")
        # 点击添加购物车
        driver.find_element(By.XPATH, '//form[@id="ECS_FORMBUY"]/ul[3]/li[2]/a/img').click()
        # 进入购物车后，点击‘结算’
        driver.find_element(By.XPATH, '//div[@class="flowBox"]/table/tbody/tr/td[2]/a/img').click()
        # 进入添加收货人信息。引入下拉类。
        # ele = driver.find_element(By.ID, "selCountries_0")  # 定位赋值,国家
        # select = Select(ele)
        # select.select_by_value("1")
        # prov = driver.find_element(By.ID, "selProvinces_0")  # 定位赋值，省份
        # select = Select(prov)
        # select.select_by_value("26")
        # citi = driver.find_element(By.ID, "selCities_0")  # 定位赋值，城市
        # select = Select(citi)
        # select.select_by_value("322")
        # dist = driver.find_element(By.ID, "selDistricts_0")  # 定位赋值，区域
        # select = Select(dist)
        # select.select_by_value("2723")
        # # 填写收货人姓名
        # driver.find_element(By.NAME, "consignee").send_keys("明明")
        # # 填写收货详细地址
        # driver.find_element(By.NAME, "address").send_keys("成都市XXXXX")
        # # 填写电话
        # driver.find_element(By.NAME, "tel").send_keys("13312341234")
        # # 填写邮箱
        # driver.find_element(By.NAME, "email").clear()
        # driver.find_element(By.NAME, "email").send_keys("1336666@qq.com")
        # # 点击添加地址
        # driver.find_element(By.NAME, "Submit").click()
        # # 选择配送地址
        driver.find_element(By.XPATH, '//table[@id="shippingTable"]/tbody/tr[2]/td[1]/input').click()
        # 选择支付方式
        driver.find_element(By.XPATH, '//table[@id="paymentTable"]/tbody/tr[2]/td[1]/input').click()

        # 要实现窗口向下滚动
        size = driver.find_element(By.TAG_NAME, "html").size
        print(size)
        # js = "window.scrollTo(0,1000)"
        js = "window.scrollTo(0,%s)" % (size["height"])  # To(o小写),(0,%s)中是逗号
        driver.execute_script(js)
        # 找到提交订单，点击
        driver.find_element(By.XPATH, '//form[@id="theForm"]/div[11]/div[2]/input[1]').click()
        # 点击提交右上角我的订单
        driver.find_element(By.XPATH, '//ul[@class="cart_info"]/li[2]/a').click()
        # 跳转页面
        handles = driver.window_handles
        driver.switch_to.window(handles[1])
        # 点击左边我的订单
        driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div/div/div/a[3]').click()
        # 点击某一条订单信息
        driver.find_element(By.XPATH, '/html/body/div[8]/div[2]/div/div/div/table/tbody/tr[4]/td[1]/a').click()
        # 查看发送/商家留言
        # driver.find_element(By.XPATH,'/html/body/div[8]/div[2]/div/div/div/table[1]/tbody/tr[1]/td[2]/a').click()
        driver.find_element(By.LINK_TEXT, "[发送/查看商家留言]").click()
        # 订单留言操作
        driver.find_element(By.NAME, "msg_title").send_keys("毛衣")
        driver.find_element(By.NAME, "msg_content").send_keys("你好")
        driver.find_element(By.CLASS_NAME, "bnt_bonus").click()
        # 删除留言
        driver.find_element(By.XPATH, '//div[@class="f_r"]/a').click()
        driver.switch_to.alert.accept()
        # 回到我的订单列表
        driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div/div/div/a[3]').click()
        # 取消订单
        driver.find_element(By.XPATH, '/html/body/div[8]/div[2]/div/div/div/table/tbody/tr[2]/td[5]/font/a').click()
        driver.switch_to.alert.dismiss()
        order = driver.find_element(By.NAME, "to_order")  # 找主订单
        select = Select(order)
        select.select_by_index(1)
        # 找从订单
        order = driver.find_element(By.NAME, "from_order")
        select = Select(order)
        select.select_by_index(2)
        # 合并订单
        driver.find_element(By.NAME, "Submit").click()
        driver.switch_to.alert.accept()
        time.sleep(5)
        driver.quit()

    def test_fifth(self):
        '''
        登录进入页面
        点击我的账户
        点击资金管理
        进行充值
        体现
        查看账户明细
        查看申请记录
        '''
        from selenium import webdriver
        import time

        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.common.by import By
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://192.168.1.120/upload/")
        driver.find_element(By.XPATH, '//font[@id="ECS_MEMBERZONE"]/a[1]').click()  # 进入登录
        driver.find_element(By.NAME, "username").send_keys("mingming")  # 输入用户名
        driver.find_element(By.NAME, "password").send_keys("123456")  # 输入密码
        driver.find_element(By.NAME, "remember").click()  # 勾选记住信息
        driver.find_element(By.NAME, "submit").click()  # 点击登录
        # 点击我的账户
        driver.find_element(By.XPATH, '//font[@id="ECS_MEMBERZONE"]/a[1]').click()
        # 点击资金管理
        driver.find_element(By.XPATH, '//div[@class="userMenu"]/a[13]').click()
        # 进入资金管理后，点充值
        driver.find_element(By.LINK_TEXT, "充值").click()
        driver.find_element(By.NAME, "amount").send_keys("1000")  # 充值金额
        driver.find_element(By.NAME, "user_note").send_keys("充点钱钱")  # 会员备注
        driver.find_element(By.NAME, "payment_id").click()  # 勾选支付方式
        driver.find_element(By.NAME, "submit").click()  # 提交申请
        # 立即使用支付宝支付
        driver.find_element(By.XPATH,
                            '//div[@class="userCenterBox boxCenterList clearfix"]/table/tbody/tr[5]/td/div/input').click()
        # 跳转支付页面后返回上一页
        handles = driver.window_handles
        driver.switch_to.window(handles[0])
        driver.find_element(By.XPATH, '//div[@class="userMenu"]/a[13]').click()
        # 点击提现 /html/body/div[8]/div[2]/div/div/div/table/tbody/tr/td/a[2]
        driver.find_element(By.LINK_TEXT, "提现").click()
        driver.find_element(By.NAME, "amount").send_keys("1000")  # 提现金额
        driver.find_element(By.NAME, "user_note").send_keys("地方三国杀")  # 会员备注
        driver.find_element(By.NAME, "submit").click()  # 提交申请
        # 返回上一页
        driver.find_element(By.XPATH, '//div[@class="boxCenterList RelaArticle"]/div/p[2]/a').click()
        # 查看账户明细
        driver.find_element(By.LINK_TEXT, "查看帐户明细").click()
        # 查看申请记录
        driver.find_element(By.LINK_TEXT, "查看申请记录").click()
        # 安全退出 /html/body/div[8]/div[1]/div/div/div/div/a[14]/img
        driver.find_element(By.XPATH, '//div[@class="userMenu"]/a[14]/img').click()

        time.sleep(3)
        driver.quit()


if __name__ == '__main__':
    # unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(TestLogin("test_frist"))
    runner = unittest.TextTestRunner()
    runner.run()


