# -*- coding: utf-8 -*-
# @Time    : 2018/8/25 19:57
# @Author  : Jeffrey
from threading import Thread

from spider.xici import XiCiSpider


class IpPool:
    ip_path = 'proxy_pool/ip.txt'

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

    def save_ip_pool(self, proxy):
        f = open(self.ip_path, 'a')
        f.writelines(str(proxy) + '\n')
        f.close()


if __name__ == '__main__':
    pool = IpPool(1, 10)
    pool.get_proxy_pool()
