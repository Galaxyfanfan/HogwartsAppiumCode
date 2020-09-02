"""
HogwartsAppiumCode - 当前Project名称;
search - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/9/2 10:53 上午 
"""
from MyTestFrameWork.page.basepage import BasePage


class Search(BasePage):
    def search(self,text):
        self.po_run('search',keyword=text)
