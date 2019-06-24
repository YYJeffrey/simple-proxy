# -*- coding: utf-8 -*-
# @Time    : 2018/8/26 14:24
# @Author  : Jeffrey
import sys
import requests

from proxy_random import ProxyRandom


def proxy_test():
    url = sys.argv[1]
    pr = ProxyRandom()
    ip = pr.get_random_ip()
    ua = pr.get_random_ua()
    test_url = url
    proxies = {'http': ip}
    headers = {'User-Agent': ua}
    print("请求地址：" + url + "\n代理地址：" + ip + "\n请求头：" + ua + "\n")
    try:
        html = requests.get(url=test_url, headers=headers, proxies=proxies).text
        print("页面内容：")
        print(html)
    except Exception as e:
        print(e.__class__)


proxy_test()
