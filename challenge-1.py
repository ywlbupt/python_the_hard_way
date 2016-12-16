#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python 3.5.2 , Anaconda
# url : http://www.pythonchallenge.com/pc/def/map.html

# K -> M
# O -> Q
# E -> G

url_1 = "map"
url = "http://www.pythonchallenge.com/pc/def/{0}.html"

map_str = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''

def map_char(s):
    if ord(s) <= ord("z") and ord(s) >= ord("a") :
        return chr((ord(s)+2-ord("a")) % (ord("z")-ord('a')+1) + ord("a"))
    else:
        return s

print(type(map_str))

chg_str=map(map_char, map_str)

# print(list(chg_str))
print("".join(chg_str))
print("url : ")
url_2 =url.format("".join(map(map_char, url_1)))
print(url_2)
# 推荐使用 string.maketrans()
