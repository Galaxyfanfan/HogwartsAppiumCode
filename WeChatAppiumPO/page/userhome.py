from appium.webdriver.common.mobileby import MobileBy

from WeChatAppiumPO.page.basepage import BasePage
from WeChatAppiumPO.page.userinfo import UserInfo


class UserHome(BasePage):
    beforenum = 0
    user_info_ele = (MobileBy.XPATH,
                                 "//*[@text='个人信息']/../../../../..//android.widget.RelativeLayout")
    def goto_user_info(self):
        self.find_and_click(self.user_info_ele)
        return UserInfo(self.driver)