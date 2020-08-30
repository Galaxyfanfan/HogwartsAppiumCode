from appium.webdriver.common.mobileby import MobileBy

from WeChatAppiumPO.page.basepage import BasePage
from WeChatAppiumPO.page.edituserinfo import EditUserInfo


class UserInfo(BasePage):
    edit_ele = (MobileBy.ID, "com.tencent.wework:id/b53")
    def goto_edit(self):
        self.find_and_click(self.edit_ele)
        return EditUserInfo(self.driver)