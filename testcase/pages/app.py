from appium import webdriver

from test_appium_object.test_qiyeweixin_tongxunlu.pages.xiaoxi_page import XiaoXiPage


class App:
    def __init__(self):
        self.driver = None
        self.start()

    def start(self):
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
        # 跳过设备初始化
        desired_caps['skipDeviceInitialization'] = 'true'
        # 启动之前不停止app
        desired_caps['dontStopAppOnReset'] = 'true'
        # 设置动态页面
        desired_caps['settings[waitForIdleTimeout]'] = 0
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def goto_xiaoxi_page(self):
        # 跳转至消息页
        return XiaoXiPage(self.driver)
