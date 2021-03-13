from appium.webdriver.common.mobileby import MobileBy

from test_appium_object.test_qiyeweixin_tongxunlu.pages.basepage import BasePage
from test_appium_object.test_qiyeweixin_tongxunlu.pages.tongxunlu_page import TongXunLuPage


class XiaoXiPage(BasePage):
    # def goto_tongxunlu_page(self):
    #     self.find_ele_click(MobileBy.XPATH,'//*[@text="通讯录"]')
    #     return TongXunLuPage(self.driver)

    def goto_tongxunlu_page(self):
        self.yaml_duqu("../pages/xiaoxi_page.yaml")
        # 跳转至通讯录页
        return TongXunLuPage(self.driver)
