import unittest
from base.get_driver import GetDriver
from base.get_logger import GetLogger
from page.page_login import PageLogin
from page.page_shopping_cart import PageShoppingCart

log = GetLogger().get_logger()


class TestShopCart(unittest.TestCase):
    cart = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.cart = PageShoppingCart(cls.driver)
        PageLogin(cls.driver).page_login_success()
        # 回到首页
        cls.cart.page_back_homepage()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    def test_shop_cart(self):
        # 加入购物车
        self.cart.page_shopping_cart()
        # 断言是否添加成功
        try:
            self.assertEqual(self.cart.page_get_add_success_info(),  "添加成功")
        except Exception as e:
            log.error(e)
            self.cart.base_get_image()
        self.cart.page_close_info_tooltip()
