#!/usr/bin/env python
# _*_ encoding:utf-8 _*_

import requests


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        headers = {
            'Host': 'blog.csdn.net',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
            # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept': 'application/json, text/javascript',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://www.baidu.com',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
        }

        res = requests.get(url, headers=headers)

        res.encoding = 'utf-8'

        return res.text

