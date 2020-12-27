from BeautifulReport import BeautifulReport
import unittest
import time
#获取用例集合
test_dir = "./test/test_case"
#与discover结合
discover = unittest.defaultTestLoader.discover(test_dir,
                                               pattern="test*.py")
#使用BeautifulReport报告运行用例，结果写入报告
BeautifulReport(discover).report(
    description=u'自动化测试报告',
    log_path="./report/",
    filename=time.strftime("%Y-%m-%d %H_%M_%S")
)

