import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage():
    logging.basicConfig(level=logging.NOTSET)  # 设置日志级别
    logging.debug(u"如果设置了日志级别为NOTSET,那么这里可以采取debug、info的级别的内容也可以显示在控制台上了")
    logging.debug(u"级别排序: CRITICAL > ERROR > WARNING > INFO > DEBUG")

    ele_black_list = [(MobileBy.ID, "com.android.packageinstaller:id/permission_allow_button")]

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def base_quit(self):
        self.driver.quit()

    def find(self, locator):
        logging.info(locator)

        # 对异常弹框处理
        try:
            find_element = self.driver.find_element(*locator)
            return find_element
        except:
            print('没找到元素，查找黑名单')
            for black in self.ele_black_list:
                eles = self.driver.find_elements(*black)
                if len(eles) > 0:
                    eles[0].click()  # 点击第一个弹窗关闭
                    break
            return self.driver.find_element(*locator)

    def finds(self, locator):
        logging.info(locator)
        return self.driver.find_elements(*locator)

    def find_and_click(self, locator):
        logging.info("点击")
        self.find(locator).click()

    def find_and_sendKeys(self, locator, value):
        logging.info("输入")
        self.find(locator).send_keys(value)

    def find_by_scroll_and_click(self, text):
        logging.info("滚动查找并点击")
        logging.info(text)

        element = (MobileBy.ANDROID_UIAUTOMATOR,
                   'new UiScrollable(new UiSelector()'
                   '.scrollable(true).instance(0))'
                   '.scrollIntoView(new UiSelector()'
                   f'.text("{text}").instance(0));')
        self.find(element).click()

    def get_toasttext(self):
        logging.info("获取toast")
        text = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        logging.info(text)

        return text
