import page
from base.base import Base
from base.get_logger import GetLogger


# 获取日志器
log = GetLogger().get_logger()


class PageOrder(Base):
    # 进入我的购物车页面
    def page_click_my_cart(self):
        log.info("点击我的购物车按钮")
        self.base_click(page.order_my_cart)

    # 判断全选框是否选中，如果没有选中则点击全选，如果选中则不做操作
    def page_if_check_all(self):
        log.info("选择所有商品")
        if not self.base_find_element(page.order_check_all).is_selected():
            self.base_click(page.order_check_all)

    # 点击去结算按钮
    def page_click_go_settlement(self):
        log.info("点击去结算按钮")
        self.base_click(page.order_go_settlement)

    # 查找收货人,解决ajax异步加载信息延迟的问题
    def page_find_person(self):
        log.info("查找收货人信息")
        self.base_find_element(page.order_person)

    # 点击提交订单按钮
    def page_click_submit_order(self):
        log.info("点击提交订单按钮")
        self.base_click(page.order_submit)

    # 获取提交成功信息
    def page_get_submit_success_info(self):
        return self.base_get_text(page.order_submit_success)

    # 提交订单组合业务方法
    def page_order(self):
        self.page_click_my_cart()
        self.page_if_check_all()
        self.page_click_go_settlement()
        # 找到收货人，代表异步加载完成
        self.page_find_person()
        self.page_click_submit_order()
