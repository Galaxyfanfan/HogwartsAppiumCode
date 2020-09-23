"""
HogwartsAppiumCode - 当前Project名称;
test_test_base64 - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/9/22 4:03 下午 
"""


from JsonDemo import test_base64

class TestBase64():
    res_data = {
        'method' : 'get',
        'url' : 'demo.txt',
        'headers' : None,
        'encoding' : 'base64'
    }

    def test_send(self):
        AR = test_base64.APIRequst()
        res = AR.send(self.res_data)
        print(res)





