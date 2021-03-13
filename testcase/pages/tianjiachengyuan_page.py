from appium.webdriver.common.mobileby import MobileBy
from test_appium_object.test_qiyeweixin_tongxunlu.pages.basepage import BasePage


class TianJiaChengYuanPage(BasePage):
    # def tianjiachengyuan(self):
    #     # 点击添加成员
    #     self.find_ele_click(MobileBy.XPATH,"//*[@text='手动输入添加']")
    #     # 点击姓名输入框并输入
    #     self.find_ele_sendkey(MobileBy.XPATH,"//*[@text='必填']","测试2")
    #     # 点击账号输入框并输入
    #     self.find_ele_sendkey(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/err']//*[@resource-id='com.tencent.wework:id/bgk']//*[@resource-id='com.tencent.wework:id/b7m']","0000002")
    #     # 点击性别输入框
    #     self.find_ele_click(MobileBy.ID,"com.tencent.wework:id/eso")
    #     # 添加隐式等待
    #     self.wait_ele_click(MobileBy.ID, "com.tencent.wework:id/bp8")
    #     # 选择性别
    #     self.find_ele_click(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/en5'and@text='女']")
    #     # 点击手机号码输入框并输入
    #     self.find_ele_sendkey(MobileBy.ID,"com.tencent.wework:id/fwi","13122222222")
    #     # 点击保存
    #     self.find_ele_click(MobileBy.ID,"com.tencent.wework:id/aj_")
    #     return True

    # 添加成员信息
    def tianjiachengyuan(self):
        self.yaml_duqu("../pages/tianjiachengyuan_page.yaml")
