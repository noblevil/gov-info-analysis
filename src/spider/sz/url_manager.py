
class UrlManager(object):
    def __init__(self):
        self.root_url = "http://www.sz.gov.cn/cn/xxgk/zfxxgj/tzgg/index.htm"
        self.page_urls = []
        self.news_urls = []
        self.error_urls = ["http://www.gz.gov.cn/gzgov/gsgg/201603/946db0381a454872a6a46b256052d0a7.shtml",
                     "http://www.gz.gov.cn/gzgov/gsgg/201511/e63c6363ad6c424a8c4360f499d7fbb2.shtml",
                     ]

    def generate_page_urls(self):
        self.page_urls.append(self.root_url)
        for x in range(1, 50):
            self.page_urls.append("http://www.sz.gov.cn/cn/xxgk/zfxxgj/tzgg/index_"+ str(x) + ".htm")
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