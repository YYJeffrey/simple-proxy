# -*- coding: utf-8 -*-
# @Time    : 2018/8/25 19:39
# @Author  : Jeffrey
import requests
import json


class UaPool:
    ua_url = 'https://fake-useragent.herokuapp.com/browsers/0.1.8'
    ua_path = 'proxy_pool/ua.txt'

    def __init__(self):
        self.ua = []

    def get_ua_pool(self):
        data = json.loads(requests.get(url=self.ua_url).text)
        ua_chrome = data['browsers']['chrome']
        ua_opera = data['browsers']['opera']
        ua_firefox = data['browsers']['firefox']
        ua_safari = data['browsers']['safari']
        ua_inter = data['browsers']['internetexplorer']
        self.ua = ua_chrome + ua_opera + ua_firefox + ua_safari + ua_inter

    def save_ua_pool(self):
        f = open(self.ua_path, 'a')
        data = self.ua
        for i in range(len(data)):
            if i < len(data) - 1:
                f.writelines(data[i] + '\n')
            else:
                f.writelines(data[i])
        f.close()


if __name__ == '__main__':
    pool = UaPool()
    pool.get_ua_pool()
    pool.save_ua_pool()
