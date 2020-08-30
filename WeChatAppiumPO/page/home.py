from appium.webdriver.common.mobileby import MobileBy


from WeChatAppiumPO.page.basepage import BasePage


class Home(BasePage):
    addressbook_element = (MobileBy.XPATH,"//*[@text='通讯录']")
    workbench_elemenet = (MobileBy.XPATH,"//*[@text='工作台']")
    mine_elemenet = (MobileBy.XPATH, "//*[@text='我']")
    def goto_addressbook(self):
        from WeChatAppiumPO.page.addressbook import AddressBook
        self.find_and_click(self.addressbook_element)
        return AddressBook(self.driver)

    def goto_workbench(self):
        from WeChatAppiumPO.page.workbench import WorkBench
        self.find_and_click(self.workbench_elemenet)
        return WorkBench(self.driver)

    def goto_mine(self):
        from WeChatAppiumPO.page.mine import Mine
        self.find_and_click(self.mine_elemenet)
        return Mine(self.driver)