#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python 3.5.2 , Anaconda
# url : http://www.pythonchallenge.com/pc/def/channel.html

import requests
import codecs
import gzip
import zipfile
import re


url_6 = "channel.html"
url = "http://www.pythonchallenge.com/pc/def/{}" 

zipfile_name = "challenge-6.zip"
head,tail = zipfile_name.split(".")

def download_zipfile():
    zipfile_url = url.format(url_6.replace("html", "zip"))
    r=requests.get(zipfile_url)
    # 二进制数据
    # print(r.content)
    with codecs.open( zipfile_name , 'wb') as f:
        f.write(r.content)
   

def zipfile_extract():
    if not zipfile.is_zipfile(zipfile_name):
        raise Exception("zip file not valid")
    with zipfile.ZipFile(zipfile_name, "r" ) as zp:
        zp.extractall(path=zipfile_name.split(".")[0])
        
def re_find_hint():
    p = re.compile("Next nothing is (?P<num>\d+)$")
    txt_num = "90052"
    while txt_num :
        print(txt_num)
        with codecs.open("/".join([head, txt_num+".txt"]), 'r') as f:
            info = f.read()
            print(info)
            m = p.search(info)
            if m:
                txt_num = m.group("num")
            else:
                txt_num = 0
# output : Collect the comment

def re_get_info():
    p = re.compile('Next nothing is (?P<num>\d+)$')
    txt_num = '90052'
    zipcomment = []
    with zipfile.ZipFile(zipfile_name, "r") as zf:
        while txt_num:
            content = zf.read(txt_num+'.txt').decode()
            m = p.search(content)
            zipcomment.append(zf.getinfo(txt_num+'.txt').comment.decode())
            if m:
                txt_num = m.group("num")
            else:
                txt_num = 0
    print("".join(zipcomment))


if __name__ == "__main__":
    download_zipfile()
    zipfile_extract() 
    # re_find_hint()
    re_get_info()

    # url_7 = "hockey.html"
