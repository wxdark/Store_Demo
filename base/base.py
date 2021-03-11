import time
from selenium.webdriver.support.wait import WebDriverWait
import page
from base.get_logger import GetLogger

# 获取日志器
log = GetLogger().get_logger()


class Base:
    def __init__(self, driver):
        log.info("[base]: 正在获取初始化drive对象:{}".format(driver))
        self.driver = driver

    def base_find_element(self, loc, timeout=30, poll=0.5):
        log.info("[base]: 查找定位{}元素".format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    def base_click(self, loc):
        log.info("[base]: 正在点击{}元素".format(loc))
        self.base_find_element(loc).click()

    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        log.info("[base]: 正在对{}元素执行清空操作".format(loc))
        el.clear()
        el.send_keys(value)

    def base_get_text(self, loc):
        log.info("[base]: 获取{}元素的文本信息".format(loc))
        return self.base_find_element(loc).text

    def base_get_image(self):
        log.info("[base]: 断言出错，调用截图")
        # 错误的日期格式可能会导致无法截图(window文件名无法使用 '' : / \ ? * < > |  等特殊符号)
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y-%m-%d_%H_%M_%S_")))

    def base_back_homepage(self):
        log.info("[base]: 登录成功返回首页")
        self.driver.get(page.URL)

    def base_switch_frame(self, name):
        log.info("切换到frame表单")
        self.driver.switch_to.frame(name)

    def base_switch_default_content(self):
        log.info("切回默认目录")
        self.driver.switch_to.default_content()

    # 切换窗口方法
    def base_switch_to_window(self, title):
        log.info("正在切换{}窗口".format(title))
        self.base_get_window_handle(title)

    # 获取指定title页面的handle方法
    def base_get_window_handle(self, title):
        # 遍历所有窗口handles
        for handle in self.driver.window_handles:
            log.info("正在遍历{}-->{}".format(handle, self.driver.window_handles))
            # 切换窗口
            self.driver.switch_to.window(handle)
            log.info("切换窗口{}".format(handle))
            # 判断当前页面title是否等于 title参数
            log.info("判断当前页面title:{}是否等于指定的title:{}".format(self.driver.title, title))
            if self.driver.title == title:
                log.info("条件成立：返回当前handle：{}".format(handle))
                return handle

    # 判断元素是否存在
    def base_element_is_exit(self, loc):
        try:
            self.base_find_element(loc, timeout=2)
            log.info("[base]: {}元素查找成功，存在页面".format(loc))
            return True  # 代表元素存在
        except:
            log.info("[base]: {}元素查找失败，不存在当前页面".format(loc))
            return False  # 代表元素不存在
