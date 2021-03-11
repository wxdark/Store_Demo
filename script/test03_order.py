import unittest

from base.base import Base
from base.get_driver import GetDriver
from base.get_logger import GetLogger
from page.page_login import PageLogin
from page.page_order import PageOrder

# 获取日志器
log = GetLogger().get_logger()


class TestOrder(unittest.TestCase):
    def setUp(self) -> None:
        # 获取driver
        self.driver = GetDriver().get_driver()
        # 调用登录成功方法
        PageLogin(self.driver).page_login_success()
        # 返回首页
        Base(self.driver).base_back_homepage()
        # 实例化PageOrder
        self.order = PageOrder(self.driver)

    def tearDown(self) -> None:
        GetDriver().quit_driver()

    def test_order(self):
        # 提交订单
        try:
            self.order.page_order()
            # 断言提交订单是否成功
            self.assertIn("提交成功", self.order.page_get_submit_success_info())
        except Exception as e:
            log.error(e)
            Base(self.driver).base_get_image()
