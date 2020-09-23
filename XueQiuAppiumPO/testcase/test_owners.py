"""
HogwartsAppiumCode - 当前Project名称;
test_owners - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/9/16 5:49 下午 
"""
import pytest
import yaml
# from requests_xml import XMLSession
from hamcrest import  *

from XueQiuAppiumPO.data.utils import Utils
from XueQiuAppiumPO.page.basepage import BasePage
from XueQiuAppiumPO.page.common_page import CommonPage

def get_capabilities():
    with open('../data/capabilities_ios.yaml') as f:
        capabilities = yaml.safe_load(f)
    return capabilities

@pytest.mark.skip
class Testlogin():
    po_file = '../data/page_owners_ios.yaml'

    def setup_class(self):
        self.app=BasePage()
        capabilities = get_capabilities()
        self.app.start(capabilities)

    def setup(self):
        pass

    def teardown_class(self):
        self.app.stop()


    @pytest.mark.parametrize('username, password',[('13777866085', '1234')])
    def test_login_common(self,username,password):
        page=CommonPage(self.po_file)
        page.login(username=username,password=password)
        page.back()

#------------------------fixture-------------------------------------------

#当一个方法上面加上 @pytest.fixture() 装饰器，就变成了fixture方法
@pytest.fixture()
def login():
    print('登录')

def test_case1(login):
    print('测试用例1---需要登录')

def test_case2():
    print('测试用例2---不需要登录')

def test_case3(login):
    print('测试用例3---需要登录')

@pytest.mark.usefixtures('login')
def test_case4():
    print('测试用例4---需要登录')
