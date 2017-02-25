#!/usr/bin/env python
# _*_ encoding:utf-8 _*_

class UrlManager(object):
    def __init__(self):
        #   列表的入口
        self.root_url = "http://www.gz.gov.cn/gzgov/gsgg/xw_list.shtml"
        #   所有的列表URL
        self.page_urls = []
        #   所有的通知公告的URL
        self.news_urls = []
        #   无法访问的通知公告的URL
        self.error_urls = ["http://www.gz.gov.cn/gzgov/gsgg/201603/946db0381a454872a6a46b256052d0a7.shtml","http://www.gz.gov.cn/gzgov/gsgg/201511/e63c6363ad6c424a8c4360f499d7fbb2.shtml"]

    def generate_page_urls(self):
        '''
        生成所有的列表URL
        '''
        self.page_urls.append(self.root_url)
        for x in range(2, 45):
            self.page_urls.append("http://www.gz.gov.cn/gzgov/gsgg/xw_list_"+ str(x) + ".shtml")
        return self.page_urls

    def add_news_urls(self, urls):
        """
        添加通知公告的UR
        """
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.news_urls.append(url)

    def get_news_urls(self):
        """取得一个通知公告的URl"""
        return self.news_urls

    def get_error_urls(self):
        """取得所有错误的通知公告的URl"""
        return self.error_urls