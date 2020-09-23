"""
HogwartsAppiumCode - 当前Project名称;
test_search - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/9/16 4:05 下午 
"""
import pytest
import yaml

from XueQiuAppiumPO.data.utils import Utils
from XueQiuAppiumPO.page.basepage import BasePage
from XueQiuAppiumPO.page.common_page import CommonPage

def get_capabilities():
    with open('../data/capabilities_ios.yaml') as f:
        capabilities = yaml.safe_load(f)
    return capabilities

class TestSearch():
    po_file = '../data/page_search.yaml'
    testcase_file = '../data/page_searchkey.yaml'
    data = Utils.from_file(testcase_file)

    def setup_class(self):
        self.app=BasePage()
        capabilities = get_capabilities()
        self.app.start(capabilities)

    def setup(self):
        pass

    def teardown_class(self):
        self.app.stop()

    #用common page代替
    @pytest.mark.parametrize(data['keys'], data['values'])
    def test_search_common(self, keyword):
        page=CommonPage(self.po_file)
        page.search(keyword=keyword)
        page.back()
