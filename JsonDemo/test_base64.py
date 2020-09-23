"""
HogwartsAppiumCode - 当前Project名称;
test_base64 - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/9/22 3:42 下午 
"""
import requests
import base64
import json

import yaml


def test_encode():
    url = 'http://127.0.0.1:9000/demo.txt'
    r = requests.get(url=url)
    res = json.loads(base64.b64decode(r.content))
    print(res)


#--------------------封装解密方法------------------------------
class APIRequst():
    def get_env(self):
        env = yaml.safe_load(open('./data/env.yaml'))
        return env

    def send(self,data:dict):
        env = self.get_env()
        default = env['default']
        url = env['environment'][default]
        url = url + ':' + env['port'] + '/' + data['url']
        print(url)
        r = requests.request(data['method'],url,headers = data['headers'])
        if data['encoding'] == 'base64':
            res = json.loads(base64.b64decode(r.content))
            return res
        elif data['encoding'] == '拿不到加密算法，发送给第三方解密':
            #把加密过后的响应值发给第三方服务，让第三方解密并返回解密后的信息
            return requests.post('url',data=r.content)












