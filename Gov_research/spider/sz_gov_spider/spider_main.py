from spider.sz_gov_spider import html_downloader
from spider.sz_gov_spider import html_parser
from spider.sz_gov_spider import url_manager
from spider.gz_gov_spider import html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self):

        #第一步先拿到所有要遍历的URL
        page_urls = self.urls.generate_page_urls()
        for page_url in page_urls:
            html_cont= self.downloader.download(page_url)
            new_urls = self.parser.paser_page_urls(html_cont)
            self.urls.add_news_urls(new_urls)

        new_urls = self.urls.get_news_urls()

        count = 1  # 计数君

        for news_url in new_urls:
            error = self.urls.get_error_urls()
            if news_url not in error:
                html_cont = self.downloader.download(news_url)
                print("craw %d : %s" % (count, news_url))
                data= self.parser.paser_data(news_url,html_cont)
                self.outputer.collect_data(data)
            count =count + 1
        self.outputer.output_html()

if __name__ == '__main__':
    obj_spider = SpiderMain()
    obj_spider.craw()
