#!/usr/bin/env python
# _*_ encoding:utf-8 _*_

class UrlManager(object):
    def __init__(self):
        #   列表的入口
        self.root_url = "http://www.dg.gov.cn/cndg/notice/news.shtml"
        #   所有的列表URL
        self.page_urls = []
        #   所有的通知公告的URL
        self.news_urls = []
        #   无法访问的通知公告的URL
        self.error_urls = []

    def generate_page_urls(self):
        '''
        生成所有的列表URL
        '''
        self.page_urls.append(self.root_url)
        for x in range(2, 101):
            self.page_urls.append("http://www.dg.gov.cn/cndg/notice/news_"+ str(x) + ".shtml")
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