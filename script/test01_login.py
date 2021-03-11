import unittest
from time import sleep

from parameterized import parameterized

from base.get_driver import GetDriver
from tool.read_json import read_json
from page.page_login import PageLogin
from base.get_logger import GetLogger

# 获取日志器
log = GetLogger().get_logger()


# 读取测试数据
def get_data(filename):
    arr = []
    for i in read_json(filename).values():
        arr.append((i.get("username"), i.get("password"), i.get("verify_code"), i.get("result")))
    return arr


class TestLogin(unittest.TestCase):
    login = None

    @classmethod
    def setUpClass(cls) -> None:
        try:
            cls.login = PageLogin(GetDriver().get_driver())
            # 点击登录链接
            cls.login.page_click_link()
        except Exception as e:
            log.info("错误信息{}".format(e))

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    @parameterized.expand(get_data("data.json"))
    def test_login_success(self, username, pwd, code, expect_result):
        # 输入用户名密码验证码点击登录按钮
        self.login.page_login(username, pwd, code)
        sleep(2)
        # 判断是否为正向用例
        if username == "13657495732" and pwd == "123456" and code == "8888":
            try:
                # 断言是否登录成功
                self.assertTrue(self.login.page_if_login())
            except Exception as e:
                log.error("错误信息{}".format(e))
                self.login.page_get_img()
                raise e
            # 点击安全退出
            self.login.page_click_quit()
            # 点击登录链接
            self.login.page_click_link()
        else:
            # 获取错误提示信息
            msg = self.login.page_get_err_info()
            print(msg)
            try:
                self.assertEqual(msg, expect_result)
            except Exception as e:
                log.error("错误信息{}".format(e))
                self.login.page_get_img()
                raise e
            # 点击错误提示框确认按钮
            self.login.page_click_ok_btn()
