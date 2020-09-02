"""
HogwartsAppiumCode - 当前Project名称;
test_search - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/9/2 10:53 上午 
"""
import pytest
import yaml

from MyTestFrameWork.testcase.test_base import TestBase

def get_name():
    with open('../datas/page_name.yaml') as f:
        datas = yaml.safe_load(f)
    return datas

class TestSearch(TestBase):
    # todo：测试数据的数据驱动
    @pytest.mark.parametrize('name',get_name())
    def test_search(self,name):
        self.app.goto_home().goto_search().search(name)

    def test_addMember(self):
        self.app.goto_home().goto_addressbook().add_member()