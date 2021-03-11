from time import sleep
import page
from base.base import Base
from base.get_logger import GetLogger


# 获取日志器
log = GetLogger().get_logger()


class PageShoppingCart(Base):
    # 打开首页
    def page_back_homepage(self):
        log.info("回到商城首页")
        sleep(2)
        self.base_back_homepage()

    # 搜索框输入商品名称
    def page_input_shop_name(self, shop_name="小米手机"):
        log.info("在搜索框输入要搜索的商品名称：{}".format(shop_name))
        self.base_input(page.shopping_search, shop_name)

    # 点击搜索按钮
    def page_click_search_btn(self):
        log.info("点击搜索按钮")
        self.base_click(page.shopping_search_btn)

    # 点击商品下方加入购物车进入商品详情页
    def page_click_shop_add_cart(self):
        log.info("正在进入商品详情页")
        self.base_click(page.shopping_detail)

    # 将商品加入购物车
    def page_add_shop_cart(self):
        log.info("添加商品到购物车")
        self.base_click(page.shopping_add_cart)

    # 获取添加成功信息
    def page_get_add_success_info(self):
        # 切换到frame窗口
        log.info("正在切换至frame表单")
        self.base_switch_frame(self.base_find_element(page.shopping_frame_name))
        # 返回添加成功信息
        return self.base_get_text(page.shopping_add_success_info)

    # 关闭信息提示框
    def page_close_info_tooltip(self):
        # 切换回默认目录
        log.info("回到默认目录")
        self.base_switch_default_content()
        # 关闭当前提示框
        log.info("关闭当前提示框")
        self.base_click(page.shopping_close_tooltip)

    # 购物车组合业务
    def page_shopping_cart(self):
        self.page_input_shop_name()
        self.page_click_search_btn()
        self.page_click_shop_add_cart()
        self.page_add_shop_cart()
