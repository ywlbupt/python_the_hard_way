#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python 3.5.2 , Anaconda
# url : http://www.pythonchallenge.com/pc/def/linkedlist.php

url_4 = "linkedlist.php"
url = "http://www.pythonchallenge.com/pc/def/linkedlist.html"
url_php = "http://www.pythonchallenge.com/pc/def/{url}?{word}={thing}"

import requests
import re

if __name__ == "__main__":

    # step 1
    # r = requests.get(url.format(url=url_4, word = "nothing", thing = "12345"))
    # step 2
    # r = requests.get(url.format(url=url_4, word = "nothing", thing = "8022"))
    # step 3
    r = requests.get(url_php.format(url=url_4, word = "nothing", thing = "63579"))
    p = re.compile(".*the next nothing is (?P<num>\d+)$")
    m = p.match(r.text)
    while m:
        print(m.group("num"))
        r = requests.get(url_php.format(url=url_4, word = "nothing", thing = m.group("num")))
        m = p.match(r.text)
    url_5 = (r.text)
    print(url_5)
    url_5 = "peak.html"
