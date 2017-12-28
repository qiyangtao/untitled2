#!/user/bin/env/python
# -*- coding: UTF-8 -*-

import urllib.request
import urllib.parse

__author__ = 'Tao Zhiqiang'


def login():
    url = 'https://www.baidu.com/?tn=02049043_69_pg'
    data = urllib.parse.urlencode({'userName': 'qiyangtao002', 'password': 'qiyangtao009'}).encode(encoding='utf-8')
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, data=data, headers=headers)
    opener = urllib.request.build_opener(urllib.request.HTTPHandler(debuglevel=1))
    s = opener.open(req)
    # s = urllib.request.urlopen(req)
    print(s.read().decode('utf-8'))
    s.close()

if __name__ == '__main__':
    login()
