from selenium.webdriver.common.by import By

# 项目服务器地址
URL = "http://127.0.0.1/index.php"
"""用户登录"""
# 登录链接
login_links = By.PARTIAL_LINK_TEXT, "登录"

# 用户名
login_username = By.CSS_SELECTOR, "#username"
# 密码
login_pwd = By.CSS_SELECTOR, "#password"
# 验证码
login_verify_code = By.CSS_SELECTOR, "#verify_code"
# 登录按钮
login_click_btn = By.CSS_SELECTOR, ".J-login-submit"
# 错误信息
login_error_info = By.CSS_SELECTOR, ".layui-layer-content"
# 错误提示框确认按钮
login_error_ok_btn = By.CSS_SELECTOR, ".layui-layer-btn0"
# 安全退出
login_quit_link = By.PARTIAL_LINK_TEXT, "安全退出"

"""购物车模块"""
# 搜索框
shopping_search = By.CSS_SELECTOR, ".ecsc-search-input"
# 搜索按钮
shopping_search_btn = By.CSS_SELECTOR, ".ecsc-search-button"
# 点击商品链接进入详情页
shopping_detail = By.PARTIAL_LINK_TEXT, "加入购物车"
# 加入购物车
shopping_add_cart = By.CSS_SELECTOR, "#join_cart"
# 添加成功提示信息
shopping_add_success_info = By.CSS_SELECTOR, ".conect-title>span"
# 关闭信息提示框
shopping_close_tooltip = By.CSS_SELECTOR, ".layui-layer-close"
# iframe表单名称
shopping_frame_name = "layui-layer-iframe1"
# 个人中心首页元素
index = By.PARTIAL_LINK_TEXT, "首页"

"""订单模块"""
# 我的购物车
# order_my_cart = By.CSS_SELECTOR, ".share-shopcar-index>span"
order_my_cart = By.CSS_SELECTOR, ".c-n"
# 全选框
order_check_all = By.CSS_SELECTOR, ".checkCartAll"
# 去结算
order_go_settlement = By.PARTIAL_LINK_TEXT, "去结算"
# 收货人 备用
order_person = By.CSS_SELECTOR, ".consignee>b"
# 提交订单
order_submit = By.CSS_SELECTOR, ".Sub-orders"

# 提交订单成功信息
order_submit_success = By.CSS_SELECTOR, ".erhuh>h3"


"""支付模块"""
# 我的订单
pay_my_order = By.PARTIAL_LINK_TEXT, "我的订单"

# 我的订单页面title
pay_switch_to_my_order = "我的订单"

# 立即支付
pay_immediately = By.PARTIAL_LINK_TEXT, "立即支付"

# 支付页面title
pay_order_payment = "订单支付-开源商城 | B2C商城 | B2B2C商城 | 三级分销 | 免费商城 | 多用户商城 | tpshop｜thinkphp shop｜TPshop 免费开源系统 | 微商城"

# 货到付款
pay_on_delivery = By.CSS_SELECTOR, "[value='pay_code=cod']"

# 确认支付方式
pay_confirm_way = By.PARTIAL_LINK_TEXT, "确认支付方式"

# 支付成功信息
pay_success_info = By.CSS_SELECTOR, ".erhuh>h3"
