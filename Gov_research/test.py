#!/usr/bin/env python
# _*_ encoding:utf-8 _*_
__author__ = 'noblevil'
__date__ = '2017/2/23 10:24'

import requests

url = "http://zmister.com"
data = requests.get(url)
print(data.status_code)
print(data.content)