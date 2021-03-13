from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestNew:
    def setup(self):
        desired_caps = {}
        # 配置平台的名字
        desired_caps['platformName'] = 'Android'
        # 配置平台的版本
        desired_caps['platformVersion'] = '6.0.1'
        # 配置平台的设备名称
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.msg.controller.MessageListActivity'
        # 不重置应用
        desired_caps['noReset'] = 'true'
        # 保证上下文列表中显示的任何webview上下文都有活动页面
        desired_caps['ensureWebviewsHavePages'] = True
        # 跳过uiautomator2 sever的安装
        desired_caps['skipSeverInstallation'] = 'true'
        # 跳过设备初始化
        desired_caps['skipDeviceInitialization'] = 'true'
        # 启动之前不停止app
        desired_caps['dontStopAppOnReset'] = 'true'
        # 设置动态页面
        desired_caps['settings[waitForIdleTimeout]'] = 0
        # 可进行中文输入
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['reseKeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def test_new(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("添加成员").instance(0));').click()
        # 点击添加成员
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 点击姓名输入框并输入
        self.driver.find_element(MobileBy.XPATH, "//*[@text='必填']").send_keys( "测试")
        # 点击账号输入框并输入
        self.driver.find_element(MobileBy.XPATH,
                              "//*[@resource-id='com.tencent.wework:id/err']//*[@resource-id='com.tencent.wework:id/bgk']//*[@resource-id='com.tencent.wework:id/b7m']").send_keys("0000001")
        # 点击性别输入框
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/eso").click()
        # 添加隐式等待
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((MobileBy.ID, "com.tencent.wework:id/bp8")))
        # 选择性别
        self.driver.find_element(MobileBy.XPATH,
                            "//*[@resource-id='com.tencent.wework:id/en5'and@text='女']").click()
        # 点击手机号输入框并输入
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/fwi").send_keys("13111111111")
        # 点击保存
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/aj_").click()