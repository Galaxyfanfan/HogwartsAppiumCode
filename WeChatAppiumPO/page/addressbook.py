from appium.webdriver.common.mobileby import MobileBy

from WeChatAppiumPO.page.basepage import BasePage


class AddressBook(BasePage):
    home_elemenet = (MobileBy.XPATH, "//*[@text='消息']")
    workbench_elemenet = (MobileBy.XPATH,"//*[@text='工作台']")
    mine_elemenet = (MobileBy.XPATH, "//*[@text='我']")
    search_element = (MobileBy.ID, "com.tencent.wework:id/hk9")

    def goto_home(self):
        from WeChatAppiumPO.page.home import Home
        self.find_and_click(self.home_elemenet)
        return Home(self.driver)

    def goto_workbench(self):
        from WeChatAppiumPO.page.workbench import WorkBench
        self.find_and_click(self.workbench_elemenet)
        return WorkBench(self.driver)

    def goto_mine(self):
        from WeChatAppiumPO.page.mine import Mine
        self.find_and_click(self.mine_elemenet)
        return Mine(self.driver)

    def goto_search(self):
        print('搜索')
        from WeChatAppiumPO.page.search import Search
        # 搜索
        self.find_and_click(self.search_element)
        return Search(self.driver)