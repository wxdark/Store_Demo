import page
from base.base import Base


class PagePayment(Base):
    # 点击我的订单
    def page_click_my_order(self, ):
        self.base_click(page.pay_my_order)

    # 选择商品点击立即支付
    def page_click_go_payment(self):
        # 切换到我的订单窗口
        self.base_switch_to_window(page.pay_switch_to_my_order)
        # 点击立即支付
        self.base_click(page.pay_immediately)

    # 选择货到付款
    def page_select_pay_on_delivery(self):
        # 切换到订单支付窗口
        self.base_switch_to_window(page.pay_order_payment)
        # 点击货到付款
        self.base_click(page.pay_on_delivery)

    # 点击确认支付方式
    def page_confirm_pay_way(self):
        self.base_click(page.pay_confirm_way)

    # 获取提交成功信息
    def page_get_pay_success_info(self):
        return self.base_get_text(page.pay_success_info)

    # 支付业务组合方法
    def page_payment(self):
        self.page_click_my_order()
        self.page_click_go_payment()
        self.page_select_pay_on_delivery()
        self.page_confirm_pay_way()
