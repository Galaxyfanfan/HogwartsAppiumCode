"""
HogwartsAppiumCode - 当前Project名称;
department - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/9/23 3:25 下午 
"""
import json

import requests
import yaml


class Department():
    dep_api = yaml.safe_load(open('../data/department_api.yaml'))
    env = yaml.safe_load(open('../data/env.yaml'))

    def base_request(self,api:dict):
        url = self.env['baseurl'] + api['url']

        #添加token
        params:dict = api['params']
        if 'access_token' in params.keys() :
            params['access_token'] = self.get_access_token()


        r = None
        if api['request'] == 'get':
            r = requests.get(url=url,params=params)
        elif api['request'] == 'post':
            url = url + '?access_token=' + self.get_access_token()
            print(params)
            r = requests.post(url=url, json=params)
        if r.status_code == 42001:
            #token 过期
            self.env['access_token'] = None
            self.edit_env()
            self.base_request(api)

        return r

    def get_access_token(self):
        token = self.env['access_token']
        print(f'获取token：{token}')

        if token != None :
            return token


        api = self.dep_api['access_token']
        r = self.base_request(api)
        if r.status_code == 200:
            res = json.loads(r.content)
            token = res['access_token']
            print(f'token接口:{token}')

            self.env['access_token'] = token
            self.edit_env()

            print('保存token')
            return token
        return None

    def edit_env(self):
        with open('../data/env.yaml', 'w', encoding='utf-8') as f:
            yaml.dump(self.env, f)

    def add(self):
        api = self.dep_api['add']
        r = self.base_request(api)
        return r

    def delete(self):
        api = self.dep_api['delete']
        r = self.base_request(api)
        return r

    def update(self):
        api = self.dep_api['update']
        r = self.base_request(api)
        return r

    def get_list(self):
        api = self.dep_api['list']
        r = self.base_request(api)
        return r