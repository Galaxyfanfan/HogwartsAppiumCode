from appium.webdriver.common.mobileby import MobileBy

from WeChatAppiumPO.page.basepage import BasePage



class AddMenberInfo(BasePage):
    name_ele = (MobileBy.XPATH, "//*[@text='姓名　']/../android.widget.EditText")
    gender_ele = (MobileBy.XPATH, "//*[@text='男']")
    man_ele = (MobileBy.XPATH, "//*[@text='男']/../..")
    women_ele = (MobileBy.XPATH, "//*[@text='女']/../..")
    phone_ele = (MobileBy.XPATH, "//*[@text='手机号']")
    save_ele = (MobileBy.XPATH, "//*[@text='保存']")

    def edit_name(self,name):
        self.find_and_sendKeys(self.name_ele,name)
        #注意 return self 具体为什么 不太清楚
        return self

    def edit_gender(self,gender):
        self.find_and_click(self.gender_ele)
        if gender == '女':
            self.find_and_click(self.women_ele)
        else:
            self.find_and_click(self.man_ele)
        return self

    def edit_phone(self,phone):
        self.find_and_sendKeys(self.phone_ele,phone)
        return self

    def save(self):
        from WeChatAppiumPO.page.userinfo import UserInfo
        self.find_and_click(self.save_ele)
        return UserInfo(self.driver)


