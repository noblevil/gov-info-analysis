
class UrlManager(object):
    def __init__(self):
        self.root_url = "http://www.gz.gov.cn/gzgov/gsgg/xw_list.shtml"
        self.page_urls = []
        self.news_urls = []

    def generate_page_urls(self):
        self.page_urls.append(self.root_url)
        for x in range(2, 45):
            self.page_urls.append("http://www.gz.gov.cn/gzgov/gsgg/xw_list_"+ str(x) + ".shtml")
        return self.page_urls

    def add_news_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.news_urls.append(url)

    def get_news_urls(self):
        return self.news_urls