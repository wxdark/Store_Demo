import unittest
from base.get_driver import GetDriver
from base.get_logger import GetLogger
from page.page_login import PageLogin
from page.page_payment import PagePayment


# 获取
log = GetLogger().get_logger()


class TestPayment(unittest.TestCase):
    def setUp(self) -> None:
        # 获取driver
        self.driver = GetDriver().get_driver()
        # 实例化PagePayment
        self.payment = PagePayment(self.driver)
        # 登录
        PageLogin(self.driver).page_login_success()

    def tearDown(self) -> None:
        # 关闭driver
        GetDriver().quit_driver()

    def test_payment(self):
        try:
            # 支付流程
            self.payment.page_payment()
            # 断言获取支付成功信息
            self.assertIn("订单提交成功", self.payment.page_get_pay_success_info())
            print(self.payment.page_get_pay_success_info())
        except Exception as e:
            self.payment.base_get_image()
            log.error(e)
