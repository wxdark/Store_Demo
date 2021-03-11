from selenium import webdriver

import page


class GetDriver:
    driver = None

    # 获取driver
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.get(page.URL)
        return cls.driver

    # 关闭driver
    @classmethod
    def quit_driver(cls):
        # 判断是否有driver,如果没有获取driver直接调用退出方法会报错
        if cls.driver:
            cls.driver.quit()
            # 退出后需重置driver,不然多个方法调用时会获取不到driver
            cls.driver = None
