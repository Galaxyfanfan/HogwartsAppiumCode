from appium.webdriver.common.mobileby import MobileBy

from WeChatAppiumPO.page.basepage import BasePage


class Mine(BasePage):
    home_elemenet = (MobileBy.XPATH, "//*[@text='消息']")
    addressbook_element = (MobileBy.XPATH,"//*[@text='通讯录']")
    workbench_elemenet = (MobileBy.XPATH,"//*[@text='工作台']")
    def goto_home(self):
        from WeChatAppiumPO.page.home import Home
        self.find_and_click(self.home_elemenet)
        return Home(self.driver)

    def goto_addressbook(self):
        from WeChatAppiumPO.page.addressbook import AddressBook
        self.find_and_click(self.addressbook_element)
        return AddressBook(self.driver)

    def goto_workbench(self):
        from WeChatAppiumPO.page.workbench import WorkBench
        self.find_and_click(self.workbench_elemenet)
        return WorkBench(self.driver)


