import time
import unittest
from tool.HTMLTestRunner import HTMLTestRunner

# 获取测试套件
suite = unittest.defaultTestLoader.discover("./")
# 报告保存路径
report_dir = "../report/report_{}.html".format(time.strftime("%Y_%m_%d %H%M%S"))
# 获取文件流，运行测试套件
with open(report_dir, "wb") as f:
    HTMLTestRunner(stream=f, title="商城自动化测试").run(suite)
