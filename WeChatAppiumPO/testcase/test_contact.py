import pytest
import yaml

from WeChatAppiumPO.page.app import AppDelegate


def get_name():
    with open("membername.yaml") as f:
        datas = yaml.safe_load(f)
        print(datas)
    return datas

def get_member():
    with open("member.yaml") as f:
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
    def test_delete_contact(self,name):
        self.search = self.main.goto_addressbook().goto_search().goto_member(name)

        if self.search:
            beforenum = self.search.beforenum
            eles = self.search.goto_user_info().goto_edit().delete_member().search_member(name)
            afternum = len(eles)
            assert afternum == beforenum - 1


    @pytest.mark.parametrize("name,gender,phone",get_member())
    def test_add_contact(self,name,gender,phone):

         mytoast = self.main.goto_addressbook().add_member().goto_hand_add_member() \
            .edit_name(name) \
            .edit_gender(gender) \
            .edit_phone(phone) \
            .save().get_toast()
         assert mytoast == "添加成功"



