"""
HogwartsAppiumCode - 当前Project名称;
test_base - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/9/2 11:18 上午 
"""
from MyTestFrameWork.page.app import APP
class TestBase():
    def setup(self):
        self.app = APP()
        self.app.start()

    def teardown(self):
        self.app.stop()