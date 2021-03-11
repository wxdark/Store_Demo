import page
from base.base import Base
from base.get_logger import GetLogger

# 获取日志器
log = GetLogger().get_logger()


class PageLogin(Base):
    # 点击登录链接
    def page_click_link(self):
        log.info("点击元素{}跳转至登录页".format(page.login_links))
        self.base_click(page.login_links)

    # 输入用户名
    def page_input_username(self, username):
        log.info("在元素{}中输入用户名：{}".format(page.login_username, username))
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        log.info("在元素{}中输入密码：{}".format(page.login_pwd, pwd))
        self.base_input(page.login_pwd, pwd)

    # 输入验证码
    def page_input_verify_code(self, code):
        log.info("在元素{}中输入验证码：{}".format(page.login_verify_code, code))
        self.base_input(page.login_verify_code, code)

    # 点击登录按钮
    def page_click_btn(self):
        self.base_click(page.login_click_btn)

    # 获取异常文本信息

    def page_get_err_info(self):
        return self.base_get_text(page.login_error_info)

    # 点击错误信息提示框确认按钮
    def page_click_ok_btn(self):
        self.base_click(page.login_error_ok_btn)

    # 判断是否登录成功
    def page_if_login(self):
        return self.base_element_is_exit(page.login_quit_link)

    # 点击安全退出
    def page_click_quit(self):
        self.base_click(page.login_quit_link)

    # 判断是否退出成功
    def page_if_quit_success(self):
        return self.base_element_is_exit(page.login_links)

    # 截图
    def page_get_img(self):
        self.base_get_image()

    # 组合业务方法
    def page_login(self, username, pwd, code):
        log.info("执行登录操作，输入用户名: {} 输入密码：{} 输入验证码：{}".format(username, pwd, code))
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_input_verify_code(code)
        self.page_click_btn()

    # 登录成功业务方法(供购物车，订单，支付模块使用)
    def page_login_success(self, username="13657495732", pwd="123456", code="8888"):
        log.info("执行登录操作，输入用户名: {} 输入密码：{} 输入验证码：{}".format(username, pwd, code))
        self.page_click_link()
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_input_verify_code(code)
        self.page_click_btn()
