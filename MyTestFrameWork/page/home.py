"""
HogwartsAppiumCode - 当前Project名称;
home - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/9/2 10:53 上午 
"""
from MyTestFrameWork.page.addressbook import AddressBook
from MyTestFrameWork.page.basepage import BasePage
from MyTestFrameWork.page.search import Search


class Home(BasePage):

    def goto_search(self):
        self.po_run('goto_search')
        return Search(self.driver)

    def goto_addressbook(self):
        self.po_run('goto_addresswork')
        return AddressBook(self.driver)
