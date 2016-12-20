#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python 3.5.2 , Anaconda
# url : http://www.pythonchallenge.com/pc/def/map.html

# deal with function string.maketrans()
# K -> M
# O -> Q
# E -> G
import string

url_1 = "map"
url = "http://www.pythonchallenge.com/pc/def/{0}.html"

map_str = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''

# string constans
# https://docs.python.org/3.5/library/string.html?highlight=ascii_lowercase#string-constants
# 产生映射的查找表，如果存在两个参数list，list的长度应该相等
table = str.maketrans(string.ascii_lowercase ,
                        string.ascii_lowercase[2:] + string.ascii_lowercase[:2])

print(str.translate(map_str, table))
print(map_str.translate(table))
