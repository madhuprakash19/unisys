from wsgiref import headers
import requests
class httpclient:
    def get(self, url, params=(), allow_redirects=True,cert='',cookies={},header={},proxies={},stream=True,timeout=3,verify=True):
        try:
            r = requests.get(url, auth=params,allow_redirects=allow_redirects,cert=cert,cookies=cookies,headers=header,proxies=proxies,stream=stream, timeout=timeout,verify=verify)
            return r
        except requests.exceptions.ReadTimeout:
            return 999
    def post(self, url,data={},json={}, allow_redirects=True,cert='',cookies={},header={},proxies={},stream=True,timeout=3,verify=True):
        try:
            r = requests.post(url,data=data,json=json,allow_redirects=allow_redirects,cert=cert,cookies=cookies,headers=header,proxies=proxies,stream=stream, timeout=timeout,verify=verify)
            return r
        except requests.exceptions.ReadTimeout:
            return 999
    def delete(self,url,allow_redirects=True, auth=(),cert='',cookies={},header={},proxies={},stream=True,timeout=3,verify=True):
        try:
            r = requests.delete(url, auth=auth,allow_redirects=allow_redirects,cert=cert,cookies=cookies,headers=header,proxies=proxies,stream=stream, timeout=timeout,verify=verify)
            return r
        except requests.exceptions.ReadTimeout:
            return 999
    def put(self, url,data={},allow_redirects=True,cert='',cookies={},header={},proxies={},stream=True,timeout=3,verify=True):
        try:
            r = requests.put(url,data=data,allow_redirects=allow_redirects,cert=cert,cookies=cookies,headers=header,proxies=proxies,stream=stream, timeout=timeout,verify=verify)
            return r
        except requests.exceptions.ReadTimeout:
            return 999
     
        



