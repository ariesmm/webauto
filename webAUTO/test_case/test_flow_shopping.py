import unittest

from page.login_page import LoginPage


class ShoppingFlowTestCase(unittest.TestCase):
    def test_shopping_flow(self):
        #登录
        login = LoginPage()
        login.login()
        #搜索
        se = Search()
        #加入购物车