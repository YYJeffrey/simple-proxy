# -*- coding: utf-8 -*-
# @Time    : 2018/8/25 20:15
# @Author  : Jeffrey
import random


class ProxyRandom:
    ip_path = 'proxy_pool/ip.txt'
    ua_path = 'proxy_pool/ua.txt'

    def get_random_ip(self):
        with open(self.ip_path, 'r') as f:
            lines = f.readlines()
            index = random.randint(0, len(lines) - 1)
            dict_line = eval(lines[index].strip())
            addr = dict_line['addr']
        return addr

    def get_random_ua(self):
        with open(self.ua_path, 'r') as f:
            lines = f.readlines()
            index = random.randint(1, len(lines) - 1)
            ua = lines[index].strip()
        return ua
