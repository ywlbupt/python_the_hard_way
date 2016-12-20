#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python 3.5.2 , Anaconda
# url : http://www.pythonchallenge.com/pc/def/equality.html

# re
# One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.
# 查找一个小写字母，它的两边都被三个大写字母包围

from bs4 import BeautifulSoup, Comment
import requests
import re

url_3 = "equality"
url = 'http://www.pythonchallenge.com/pc/def/{0}.html'

def get_url_text(url):
    r = requests.get(url, timeout = 30)
    return r.text

def filter_w(w):
    return ord(w) <= ord('z') and ord(w) >= ord('a')

if __name__ == "__main__":
    soup = BeautifulSoup(get_url_text(url.format(url_3)), "html.parser")
    # fing_all 判断是否为Comment 类型
    comments = soup.find_all(text=lambda text:isinstance(text, Comment))
    # 获取注释内容 
    tip_text = comments[0]

    p = re.compile("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]")
    ms = p.finditer(tip_text)
    for m in  ms:
        print(m.group(0))
    # url_4 = "".join([m.group(1) for m in ms])
    # print(url.format(url_4))

    # http://www.pythonchallenge.com/pc/def/linkedlist.html
    # redirect to http://www.pythonchallenge.com/pc/def/linkedlist.php
