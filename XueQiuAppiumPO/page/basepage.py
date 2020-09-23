"""
HogwartsAppiumCode - 当前Project名称;
basepage - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/9/2 10:53 上午 
"""
import yaml
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
import logging

class BasePage():
    _current_element:WebElement = None
    _current_elements = []
    _driver:WebDriver = None

    logging.basicConfig(level=logging.NOTSET)  # 设置日志级别

    def __init__(self,po_file=None):
        print(f'file:{po_file}')
        if po_file is not None:
            self._po_file = po_file

    #对应的函数不需要实例化,不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
    @classmethod
    def start(cls,capabilities):
        logging.info('启动')

        cap = capabilities['capabilities']
        url = capabilities['url']

        if cls._driver == None:
            cls._driver = webdriver.Remote(url, cap)
            cls._driver.implicitly_wait(10)
        else:
            cls._driver.launch_app()

        return cls

    def stop(self):
        logging.info('退出')
        BasePage._driver.quit()

    def find(self,locator):
        logging.info(f'查找 {locator}')
        self._current_element = BasePage._driver.find_element(*locator)
        return self

    def finds(self,locator):
        logging.info(f'查找 {locator}')
        self._current_elements = BasePage._driver.find_elements(*locator)
        BasePage._driver.find_element_by_ios_predicate()
        return self

    def click(self):
        logging.info('点击')
        self._current_element.click()
        return self

    def send_keys(self,value):
        logging.info('输入：' + value)
        self._current_element.send_keys(value)
        return self

    def back(self):
        logging.info('返回')
        BasePage._driver.back()
        return self

    def po_run(self,po_method, **kwargs):#可以接收任意数量关键词参数的kwargs
        #po_method:yaml文件中的key
        # todo：测试步骤的数据驱动
        logging.debug(f"po_run {po_method} {kwargs}")
        with open(self._po_file) as f:
            eles = yaml.safe_load(f)
            if po_method in eles.keys():
                for step in eles[po_method]:
                    # 如果step 是字典
                    if isinstance(step,dict):
                        for key in step.keys():
                            if key == 'id':
                                locator = (MobileBy.ID,step[key])
                                self.find(locator)
                            if key == 'xpath':
                                locator = (MobileBy.XPATH,step[key])
                                print(locator)
                                self.find(locator)
                            if key == 'css':
                                locator = (MobileBy.CSS_SELECTOR,step[key])
                                print(locator)
                                self.find(locator)

                            elif key == 'click':
                                self.click()

                            elif key == 'send_keys':
                                text = str(step[key])
                                for k,v in kwargs.items():
                                    text = text.replace('${' + k + '}',v)
                                self.send_keys(text)

                            elif key == 'scroll':
                                text = str(step[key])
                                self.find_by_scroll(text)
                            # todo: 更多关键词
                    else:
                        logging.info('格式错误')


            else:
                logging.info('method name error')


    def find_by_scroll(self,text):
        element = (MobileBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector()'
                   '.scrollable(true).instance(0))'
                   '.scrollIntoView(new UiSelector()'
                   f'.text("{text}").instance(0));')
        self.find(element)
        return self

    def get_toast(self):
        element = (MobileBy.XPATH,"//*[@class='android.widget.Toast']")
        self.find(element)
        text = self._current_element.text

        return text






