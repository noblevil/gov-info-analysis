#!/usr/bin/env python
# _*_ encoding:utf-8 _*_

class UrlManager(object):
    def __init__(self):
        #   列表的入口
        self.root_url = "http://www.zs.gov.cn/main/zwgk/list/index.action?did=91"
        #   所有的列表URL
        self.page_urls = []
        #   所有的通知公告的URL
        self.news_urls = []
        #   无法访问的通知公告的URL
        #"http://www.zs.gov.cn/main/zwgk/newsview/index.action?id=1732"
        self.error_urls = [
                           "http://www.zs.gov.cn/main/zwgk/newsview/index.action?id=1823",
                           "http://www.zs.gov.cn/main/zwgk/newsview/index.action?id=1844",
                           "http://www.zs.gov.cn/main/zwgk/newsview/index.action?id=1877",
                           "http://www.zs.gov.cn/main/zwgk/newsview/index.action?id=1889",
                           "http://www.zs.gov.cn/main/zwgk/newsview/index.action?id=1902",
                           "http://www.zs.gov.cn/main/zwgk/newsview/index.action?id=1927",
                           "http://www.zs.gov.cn/main/zwgk/newsview/index.action?id=1945",
                           "http://www.zs.gov.cn/main/zwgk/newsview/index.action?id=1947",]

    def generate_page_urls(self):
        '''
        生成所有的列表URL
        '''
        self.page_urls.append(self.root_url)
        for x in range(1, 20):
            self.page_urls.append("http://www.jiangmen.gov.cn/zwgk/tzgg/default_"+ str(x) + ".html")
        return self.page_urls

    def generate_news_urls(self):
        for x in range(1675,3000):
            self.news_urls.append("http://www.zs.gov.cn/main/zwgk/newsview/index.action?id=" + str(x))
        return self.news_urls


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