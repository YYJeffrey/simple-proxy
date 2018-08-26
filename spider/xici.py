# -*- coding: utf-8 -*-
# @Time    : 2018/8/25 19:11
# @Author  : Jeffrey
import requests
from bs4 import BeautifulSoup


class XiCiSpider:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.1'
                      '01 Safari/537.36'
    }
    timeout = 2.5

    def __init__(self, page):
        self.page = page
        self.addrs = []
        self.html = ''

    def get_html(self):
        xici_url = 'http://www.xicidaili.com/nn/'
        url = xici_url + str(self.page)
        html = requests.get(url=url, headers=self.headers).text
        self.html = html

    def parse_html(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        table = soup.find('table', id='ip_list')
        tr_re = table.findAll('tr')[1:]
        return tr_re

    def download_data(self, tr_re):
        for t in range(len(tr_re)):
            data_tr = tr_re[t]
            if self._is_fast(data_tr):
                td = data_tr.findAll('td')
                ip = td[1].get_text()
                port = td[2].get_text()
                protocol = str.lower(td[5].get_text())
                addr = 'http://' + ip + ':' + port
                data = {'protocol': protocol, 'ip': ip, 'port': port, 'addr': addr}
                can_use = self._valid_proxy(data)
                if can_use:
                    self.addrs.append(data)
                print((data, can_use))

    @staticmethod
    def _is_fast(tr_re):
        bar_inner = tr_re.findAll('div', class_='bar_inner')
        for index in range(len(bar_inner)):
            if 'fast' not in bar_inner[index]['class']:
                return False
        return True

    def _valid_proxy(self, proxy):
        test_ip_url = 'http://icanhazip.com'
        test_code_url = 'https://www.baidu.com'
        proxies = {'http': proxy['addr']}
        try:
            html_ip = requests.get(url=test_ip_url, headers=self.headers, proxies=proxies, timeout=self.timeout).text
            cur_ip = html_ip.strip()
            if cur_ip == proxy['ip']:
                html_baidu = requests.get(url=test_code_url, headers=self.headers, proxies=proxies,
                                          timeout=self.timeout)
                if html_baidu.status_code == 200:
                    return True
            return False
        except Exception as e:
            print(e.__class__)
            return False

# if __name__ == '__main__':
#     spider = XiCiSpider(3)
#     spider.get_html()
#     tr = spider.parse_html()
#     spider.download_data(tr)
#     for i in range(len(spider.addrs)):
#         print(spider.addrs[i])
