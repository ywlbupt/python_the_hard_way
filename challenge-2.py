#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python 3.5.2 , Anaconda
# url : http://www.pythonchallenge.com/pc/def/ocr.html

# find rare character in page sourcecode

from bs4 import BeautifulSoup, Comment
import requests
import re

url_2 = "ocr"
url = 'http://www.pythonchallenge.com/pc/def/{0}.html'

def get_url_text(url):
    r = requests.get(url, timeout = 30)
    return r.text

def filter_w(w):
    return ord(w) <= ord('z') and ord(w) >= ord('a')

if __name__ == "__main__":
    soup = BeautifulSoup(get_url_text(url.format(url_2)), "html.parser")
    # fing_all 判断是否为Comment 类型
    comments = soup.find_all(text=lambda text:isinstance(text, Comment))
    # 获取第二注释
    get_tip_text = comments[1]
    # 列表提取 filter
    url_3 ="".join(filter(filter_w, get_tip_text))
    print(url.format(url_3))

    # http://www.pythonchallenge.com/pc/def/equality.html
