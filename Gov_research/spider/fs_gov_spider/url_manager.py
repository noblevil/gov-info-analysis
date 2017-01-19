
class UrlManager(object):
    def __init__(self):
        self.root_url = "http://www.foshan.gov.cn/zwgk/gggs/index.html"
        self.page_urls = []
        self.news_urls = []
        self.error_urls = []

    def generate_page_urls(self):
        self.page_urls.append(self.root_url)
        for x in range(1, 25):
            self.page_urls.append("http://www.foshan.gov.cn/zwgk/gggs/index_"+ str(x) + ".html")
        return self.page_urls

    def add_news_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.news_urls.append(url)

    def get_news_urls(self):
        return self.news_urls

    def get_error_urls(self):
        return self.error_urls