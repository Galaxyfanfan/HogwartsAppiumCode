from appium.webdriver.common.mobileby import MobileBy

from WeChatAppiumPO.page.addmemberinfo import AddMenberInfo
from WeChatAppiumPO.page.basepage import BasePage



class AddMember(BasePage):
    hand_add_member_ele = (MobileBy.XPATH,"//*[@text='手动输入添加']/../..")
    def goto_hand_add_member(self):
        self.find_and_click(self.hand_add_member_ele)
        return AddMenberInfo(self.driver)