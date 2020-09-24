"""
HogwartsAppiumCode - 当前Project名称;
test_department - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/9/23 3:36 下午 
"""
import json

from WeChatDepJson.page.department import Department


class TestDepartment():
    def setup(self):
        self.dep = Department()

    def test_add(self):
        r = self.dep.add()
        data = json.loads(r.content)
        print(data)
        assert data['errcode'] == 0

    def test_delete(self):
        r = self.dep.delete()
        data = json.loads(r.content)
        print(data)
        assert data['errcode'] == 0

    def test_update(self):
        r = self.dep.update()
        data = json.loads(r.content)
        print(data)
        assert data['errcode'] == 0

    def test_list(self):
        r = self.dep.get_list()
        data = json.loads(r.content)
        print(data)
        assert data['errcode'] == 0

