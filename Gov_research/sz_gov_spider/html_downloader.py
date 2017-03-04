#!/usr/bin/env python
# _*_ encoding:utf-8 _*_

import requests


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        import  urllib2
        # 抓取网页html

        html = urllib2.urlopen(url, timeout=30).read()

        html = html.decode('gb2312', 'ignore').encode('utf-8')

        return html

