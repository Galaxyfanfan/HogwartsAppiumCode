"""
HogwartsAppiumCode - 当前Project名称;
app - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/9/2 10:52 上午 
"""

from MyTestFrameWork.page.basepage import BasePage
from MyTestFrameWork.page.home import Home



class APP(BasePage):

    def goto_home(self) -> Home:
        return Home(self.driver)