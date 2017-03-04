#!/usr/bin/env python
# _*_ encoding:utf-8 _*_

import requests


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
        }

        res = requests.get(url, headers=headers)

        return res.content.decode(res.apparent_encoding,'replace').encode('utf-8')

