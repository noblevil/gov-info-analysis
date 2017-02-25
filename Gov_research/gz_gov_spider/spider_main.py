#!/usr/bin/env python
# _*_ encoding:utf-8 _*_

from gz_gov_spider import html_downloader
from gz_gov_spider import html_parser
from gz_gov_spider import url_manager
from gz_gov_spider import html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self):

        #   第一步先拿到所有要遍历的列表URL
        page_urls = self.urls.generate_page_urls()

        #   第二步拿到所有的通知公告的URl
        for page_url in page_urls:
            html_cont= self.downloader.download(page_url)
            #   按列表页解析HTML
            new_urls = self.parser.paser_page_urls(html_cont)
            self.urls.add_news_urls(new_urls)

        #   取出通知公告的URL
        new_urls = self.urls.get_news_urls()
        count = 1  # 计数君

        for news_url in new_urls:
            #   去除错误的URls
            error = self.urls.get_error_urls()

            if news_url not in error:
                #   正在爬取的通知公告的URL
                print("craw %d : %s" % (count, news_url))
                #   下载HTML
                html_cont = self.downloader.download(news_url)
                #   按通知公告解析HTML
                data= self.parser.paser_data(news_url,html_cont)
                #   收集数据
                self.outputer.collect_data(data)

            #   计数+1
            count += 1

        self.outputer.output_html()

if __name__ == '__main__':
    obj_spider = SpiderMain()
    obj_spider.craw()
