#!/usr/bin/env python
# _*_ encoding:utf-8 _*_

from zs_gov_spider import html_downloader
from zs_gov_spider import html_parser
from zs_gov_spider import url_manager
from zs_gov_spider import html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self):




        #   直接生成所有通知公告的URL
        new_urls = self.urls.generate_news_urls()
        count = 1
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
