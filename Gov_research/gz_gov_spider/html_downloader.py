#!/usr/bin/env python
# _*_ encoding:utf-8 _*_

import requests


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        res = requests.get(url)

        res.encoding = 'utf-8'

        return res.text

