import pytest
import yaml

from WeChatAppiumPO.page.app import AppDelegate


def get_name():
    with open("membername.yaml") as f:
        datas = yaml.safe_load(f)
        print(datas)
    return datas

class TestContact():
    def setup(self):
        self.app = AppDelegate()
        self.main = self.app.start().goto_home()

    def teardown(self):
        self.app.stop()


    @pytest.mark.parametrize("name",get_name())
    def test_deleteContact(self,name):
        self.search = self.main.goto_addressbook().goto_search().goto_member(name)

        if self.search:
            beforenum = self.search.beforenum
            eles = self.search.goto_user_info().goto_edit().delete_member().search_member(name)
            afternum = len(eles)
            assert afternum == beforenum - 1



