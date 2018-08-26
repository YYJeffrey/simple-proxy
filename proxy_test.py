# -*- coding: utf-8 -*-
# @Time    : 2018/8/26 14:24
# @Author  : Jeffrey
import requests

from proxy_random import ProxyRandom


def proxy_test():
    pr = ProxyRandom()
    test_url = 'http://angular.ink/project/introduction'
    proxies = {'http': pr.get_random_ip()}
    headers = {'User-Agent': pr.get_random_ua()}
    html = requests.get(url=test_url, headers=headers, proxies=proxies).text
    print(html)


try:
    proxy_test()
except Exception as e:
    print(e)
