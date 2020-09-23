"""
HogwartsAppiumCode - 当前Project名称;
test_auth - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/9/22 11:24 上午 
"""
import requests
from requests.auth import HTTPBasicAuth
def test_oauth():
    url = 'http://httpbin.testing-studio.com/basic-auth/jammy/123456'
    r = requests.get(url = url, auth = HTTPBasicAuth('jammy','123456'))
    print(r.headers)
    print(r.text)
