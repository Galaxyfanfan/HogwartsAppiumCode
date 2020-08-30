from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from WeChatAppiumPO.page.basepage import BasePage



class EditUserInfo(BasePage):
    delete_text = '删除成员'
    delete_ele = (MobileBy.ID, "com.tencent.wework:id/bfe")
    def delete_member(self):
        from WeChatAppiumPO.page.search import Search

        #滚动查找 删除成员
        self.find_by_scroll_and_click(self.delete_text)
        self.find_and_click(self.delete_ele)
        print('点击删除')
        sleep(2)
        return Search(self.driver)
