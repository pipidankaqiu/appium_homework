from test_appium_object.test_qiyeweixin_tongxunlu.pages.app import App


class TestTongXuLu:
    def setup(self):
        self.app = App()

    def test_tongxunlu(self):
        self.app.goto_xiaoxi_page().goto_tongxunlu_page().goto_tianjiachengyuan_page().tianjiachengyuan()
