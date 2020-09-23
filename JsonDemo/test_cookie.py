"""
HogwartsAppiumCode - 当前Project名称;
test_cookie - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/9/22 10:55 上午 
"""

import requests

def test_cookie():
    url = 'http://httpbin.testing-studio.com/cookies'
    headers = {'user':'jammy'}
    cookies_data = {
        'token':'skdjlakjdl',
        'uuid':'123'
    }
    r = requests.get(url=url, headers = headers, cookies = cookies_data)
    # print(r.text)
    print(r.request.headers)