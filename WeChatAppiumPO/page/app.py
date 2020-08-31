from WeChatAppiumPO.page.basepage import BasePage
from  WeChatAppiumPO.page.home import Home
from appium import webdriver

class AppDelegate(BasePage):
    def start(self):
        if self.driver == None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "hogwarts"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.WwMainActivity"
            caps["noReset"] = "true"

            self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', caps)
            self.driver.implicitly_wait(10)
        else:
            # 启动 caps 里面设置的appPackage appActivity
            self.driver.launch_app()
            # 启动 任何一个包和activity
            # self.driver.start_activity()

        #如果想要链式调用本身的方法 需要return self
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def close(self):
        self.driver.close_app()

    def stop(self):
        self.base_quit()

    def goto_home(self) -> Home:
        return Home(self.driver)

