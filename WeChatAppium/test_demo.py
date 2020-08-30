from typing import List

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from time import sleep
import pytest
from appium.webdriver.common.touch_action import TouchAction


class TestWeChat():
    def setup(self):

        # {
        #     "noReset": true,
        #     "platformName": "android",
        #     "deviceName": "hogwarts",
        #     "appPackage": "com.tencent.wework",
        #     "appActivity": ".launch.WwMainActivity"
        # }
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.WwMainActivity"
        caps["noReset"] = "true"

        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_addMember(self):
        name = 'haha12'
        gender = "男"
        phone = "13711223324"

        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()

        # self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成员']").click()
        #因为添加成员按钮在列表最下面 所以改为滚动查找
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()

        self.driver.find_element_by_xpath("//*[@text='手动输入添加']/../..").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='姓名　']/../android.widget.EditText").send_keys(name)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='性别']/../android.widget.RelativeLayout").click()
        if gender == "女":
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']/../..").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']/../..").click()

        self.driver.find_element(MobileBy.XPATH,"//*[@text='手机号']").send_keys(phone)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='保存']").click()

        sleep(1)
        print(self.driver.page_source)
        toastText = self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.Toast']")
        assert toastText == "添加成功"

    @pytest.mark.skip
    def test_deleteMember(self):
        name = 'hhhh'

        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()#点击通讯录
        self.driver.find_element(MobileBy.XPATH,f"//*[@text='{name}']/../../../..").click()#点击用户名
        self.driver.find_element(MobileBy.XPATH,"//*[@text='个人信息']/../../../../..//android.widget.RelativeLayout").click()#点击更多
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/b53").click()#点击 编辑成员

        action = TouchAction(self.driver)

        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width / 2)
        y_start = int(height * 4 / 5)
        y_end = int(height * 1 / 5)
        sleep(3)
        action.press(x=x1, y=y_start).wait(1000).move_to(x=x1, y=y_end).release().perform()#滑动到底部
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/e_1").click()#点击删除
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/bfe").click()#点击确定 删除
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hk9").click()  #搜索
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/g75").send_keys(name)  # 输入搜索内容

        eles = self.driver.find_elements(MobileBy.XPATH,f'//*[@class="android.widget.TextView" and @text="{name}"]')
        print(eles)
        print(len(eles))

        assert len(eles) > 0

    def test_deleteMember2(self):
        name = 'hhhh'

        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()#点击通讯录
        #点击搜索
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hk9").click()  # 搜索
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/g75").send_keys(name)  # 输入搜索内容
        sleep(2)
        eles = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        beforenum = len(eles)
        if beforenum < 2:
            print("没有可删除的人员")
            return

        eles[1].click()

        # self.driver.find_element(MobileBy.XPATH,f"//*[@text='{name}']/../../../..").click()#点击用户名
        self.driver.find_element(MobileBy.XPATH,"//*[@text='个人信息']/../../../../..//android.widget.RelativeLayout").click()#点击更多
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/b53").click()#点击 编辑成员

        # action = TouchAction(self.driver)
        # window_rect = self.driver.get_window_rect()
        # width = window_rect['width']
        # height = window_rect['height']
        # x1 = int(width / 2)
        # y_start = int(height * 4 / 5)
        # y_end = int(height * 1 / 5)
        # sleep(3)
        # action.press(x=x1, y=y_start).wait(1000).move_to(x=x1, y=y_end).release().perform()#滑动到底部
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/e_1").click()  # 点击删除

        #滑动改为滚动查找
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("删除成员").instance(0));').click()


        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/bfe").click()#点击确定 删除

        sleep(2)
        eles1 = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        afternum = len(eles1)
        assert afternum == beforenum - 1
