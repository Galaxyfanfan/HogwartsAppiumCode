"""
HogwartsAppiumCode - 当前Project名称;
mitm - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/9/16 11:17 上午 
"""
from mitmproxy import http

def request(flow:http.HTTPFlow):
    #类似Charles的map local
    with open('getLastApp') as f:
        if flow.request.pretty_url == 'https://www.baidu.com/':
            # 如果请求是这个，响应替换成本地文件
            # cls,
            # status_code: int = 200,
            # content: Union[bytes, str] = b"",
            # headers: Union[Dict[str, AnyStr], Iterable[Tuple[bytes, bytes]]] = ()
            flow.response = http.HTTPResponse.make(
                200,
                f.read(),
                {'Content-Type': 'application/json'}
            )

def response(flow:http.HTTPFlow):
    if flow.request.pretty_url == 'https://www.baidu.com/':
        # 如果请求是这个，替换响应文本
        flow.response.text = 'xxxxxx'
