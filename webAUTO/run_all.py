# 批量执行用例生成报告
import unittest
from HTMLTestRunner import HTMLTestRunner
# 批量执行用例
import time

discover = unittest.defaultTestLoader.discover(start_dir='test_case',
                                               pattern='test*.py',
                                               top_level_dir=None)
time_str = time.strftime("%Y%m%d%H%M", time.localtime())
report_name = 'report/report-' + time_str + '.html'
print(report_name)
with open(report_name, 'wb') as f:
    runner = HTMLTestRunner(stream=f,
                            title="ecshop自动化测试",
                            description="自动化测试报告详情")
    runner.run(discover)
