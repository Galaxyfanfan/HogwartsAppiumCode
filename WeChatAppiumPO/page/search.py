from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from WeChatAppiumPO.page.basepage import BasePage
from WeChatAppiumPO.page.userhome import UserHome


class Search(BasePage):
    search_element = (MobileBy.ID, "com.tencent.wework:id/g75")
    def search_member(self,name):
        print('查找成员')
        self.find_and_sendKeys(self.search_element,name)
        sleep(2)
        eles = self.finds((MobileBy.XPATH, f"//*[@text='{name}']"))
        return eles

    def goto_member(self,name):

        eles = self.search_member(name)
        beforenum = len(eles)
        if beforenum < 2:
            print("没有可删除的人员")
            return
        else:
            eles[1].click()
            user_home = UserHome(self.driver)
            user_home.beforenum = beforenum
            return user_home

