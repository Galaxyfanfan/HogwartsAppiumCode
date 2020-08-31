from appium.webdriver.common.mobileby import MobileBy

from WeChatAppiumPO.page.basepage import BasePage


class Mine_Commuting(BasePage):
    home_address_ele = (MobileBy.ID,'d78')
    def commuting(self):
        print('通勤')
        self.find_and_click(self.home_address_ele)