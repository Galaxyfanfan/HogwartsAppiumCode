"""
HogwartsAppiumCode - 当前Project名称;
addressbook - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/9/2 5:08 下午 
"""
from MyTestFrameWork.page.basepage import BasePage


class AddressBook(BasePage):
    def add_member(self):
        self.po_run('addmember')
