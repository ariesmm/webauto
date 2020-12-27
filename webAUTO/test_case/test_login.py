import unittest
from  page.login_page import LoginPage

class LoginTestCase(unittest.TestCase):
    def test_login_a(self):
        '''用户名合法登录'''
        lp = LoginPage()
        actual = lp.login("luoliming","llm,1402726912")
        self.assertEqual('luoliming',actual)

    def test_login_b(self):
        '''用户名为空'''
        Ip = LoginPage()
        actual = Ip.login("","llm,1402726912")
        self.assertEqual('luoliming',actual)


if __name__ == '__main__':
    unittest.main()
