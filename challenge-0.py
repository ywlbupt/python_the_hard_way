#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python 3.5.2 , Anaconda
# url : http://www.pythonchallenge.com/pc/def/0.html
# Tips : 计算屏幕上的数字的值，替代url中的数字0

import math
import webbrowser

if __name__ == "__main__":
    url = r'http://www.pythonchallenge.com/pc/def/{0}.html'
    num = pow(2,38)
    url = url.format(num)

    # 在web 浏览器中打开 url
    # webbrowser._tryorder 获取可用 browser list
    webbrowser.open(url)
