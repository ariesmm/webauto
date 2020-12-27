import unittest
from HTMLTestRunner import HTMLTestRunner

discover = unittest.defaultTestLoader.discover(start_dir='./',
                                               pattern='test*.py',
                                               top_level_dir=None)
f = open('report.html', 'wb+')
runner = HTMLTestRunner(stream=f,
                        title="web自动化",
                        description="自动化测试报告详情")
runner.run(discover)
f.close()
