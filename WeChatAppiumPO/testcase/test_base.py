from WeChatAppiumPO.page.app import AppDelegate


class TestBase():
    def setup(self):
        self.app = AppDelegate()
        self.main = self.app.start().goto_home()

    def teardown(self):
        self.app.stop()