#!/user/bin/env/python
# -*- coding: UTF-8 -*-
import urllib.request
import urllib.parse

__author__ = 'Tao Zhiqiang'


def print_list(list):
    for i in list:
        print(i)


def demo():
    s = urllib.request.urlopen('http://www.baidu.com/')
    # print(s.read())
    # for i in range(10):
    #     print('line %d: %s' % (i + 1, s.readline()))
    # print(s.readlines())
    # print_list(s.info().items())
    # print(s.info().get_content_type())
    # print_list(dir(s.info())) #查看所有的方法

# 打印当前的下载进度
def progress(blk, blk_size, total_size):
    print('%d/%d - %.02f%%' % (blk*blk_size, total_size, float(blk*blk_size)*100/total_size))


def retrieve():
    (fname, msg) = urllib.request.urlretrieve('http://65.ierge.cn/13/202/405495.mp3', 'index.mp3', reporthook=progress)
    # print(fname)
    # print_list(msg.items())

# 对数据进行转码
def urlencode():
    parms = {'score': 100, 'age': 10, 'sex': '男', 'name': 'toms'}
    print(urllib.parse.parse_qs(urllib.parse.urlencode(parms)))

if __name__ == '__main__':
    urlencode()
