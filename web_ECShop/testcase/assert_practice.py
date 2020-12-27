import unittest
class MyTest(unittest.TestCase):

    def setup(self) :
        print("ss")
    def tearDown(self):
        print("ok")

    def test_first(self):
        print("第一条")
        expected = ['hello']
        actual = ['hello','nihao']
        self.assertIn(expected,actual)

    def test_second(self):
        print("第二条")
        expected = 5
        actual = (12,54,5)
        self.assertIn(expected,actual)

