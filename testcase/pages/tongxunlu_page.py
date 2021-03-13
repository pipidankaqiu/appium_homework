from appium.webdriver.common.mobileby import MobileBy

from test_appium_object.test_qiyeweixin_tongxunlu.pages.basepage import BasePage
from test_appium_object.test_qiyeweixin_tongxunlu.pages.tianjiachengyuan_page import TianJiaChengYuanPage


class TongXunLuPage(BasePage):
    # def goto_tianjiachengyuan_page(self):
    #     self.huadong_ele_click(MobileBy.ANDROID_UIAUTOMATOR,"添加成员")
    #     return TianJiaChengYuanPage(self.driver)

    def goto_tianjiachengyuan_page(self):
        self.yaml_duqu("../pages/tongxunlu_page.yaml")
        # 跳转至添加成员页
        return TianJiaChengYuanPage(self.driver)
