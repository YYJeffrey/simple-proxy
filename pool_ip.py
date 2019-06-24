# -*- coding: utf-8 -*-
# @Time    : 2018/8/25 19:57
# @Author  : Jeffrey
from threading import Thread

from spider.xici import XiCiSpider

IP_PATH = 'proxy_pool/ip.txt'


class IpPool:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_single_ip_pool(self, page):
        spider = XiCiSpider(page)
        spider.get_html()
        tr = spider.parse_html()
        spider.download_data(tr)
        proxy = spider.addrs
        if len(proxy) > 0:
            for i in range(len(proxy)):
                self.save_ip_pool(proxy[i])

    def get_proxy_pool(self):
        for page in range(self.start, self.end):
            t = Thread(target=self.get_single_ip_pool, args=(page,))
            t.start()

    @staticmethod
    def save_ip_pool(proxy):
        f = open(IP_PATH, 'a')
        f.writelines(str(proxy) + '\n')
        f.close()


if __name__ == '__main__':
    f = open(IP_PATH, 'r+')
    f.truncate()    # 清空文件
    f.close()
    pool = IpPool(1, 10)
    pool.get_proxy_pool()
