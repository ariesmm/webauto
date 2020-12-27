import unittest

from lib.data_lib import read_csv
from page.register_page import RegisterPage


class RegisterTestCase(unittest.TestCase):
    def test_login_a(self):
        '''注册'''
        PP = RegisterPage()
        file_name = r"E:\海德41\python\webauto\webAUTO\data\register.csv"
        data = read_csv(file_name)
        username = data[1]
        email = username + "@126.com"
        passwd = username + "123"
        confirm_passwd = passwd
        actual = PP.register(username, email, passwd, confirm_passwd)

        self.assertEqual(username, actual)


if __name__ == '__main__':
    unittest.main()
