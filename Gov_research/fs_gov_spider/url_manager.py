
class UrlManager(object):
    def __init__(self):
        self.root_url = "http://www.foshan.gov.cn/zwgk/gggs/index.html"
        self.page_urls = []
        self.news_urls = []
        self.error_urls = ["http://www.foshanepb.gov.cn/zwgk/wzgg/201701/t20170105_6093376.html",
                           "http://www.foshan.gov.cn/hdjl/myzj/zxdc/201505/t20150515_5118504.html",
                           "http://www.fswsj.gov.cn/wsdt/wsyw/video/201501/t20150114_5018788.html",
                           "http://www.fswsj.gov.cn/wsdt/wsyw/video/201412/t20141224_4921603.html",
                           "http://www.citygf.com/hdzt/2014zt/fsqzlx/04/201409/t20140928_5347771.html",
                           "http://172.16.5.70/pub/fssbxx/ztzl/tdzyt/xxncylbx/zcfg/201402/t20140208_4534522.html",
                           "http://www.foshan.gov.cn/hdjl/myzj/zwgz/201312/t20131225_4506065.html",
                           "http://www.fsgoa.cn/tzgg/201312/t20131211_4495446.html",
                           "http://www.fsjsjd.gov.cn/zlj_hdzt/zlj_ggtz/201310/t20131014_4438930.html",
                           "http://www.fswater.gov.cn/gonggao/201304/t20130403_4276408.html",
                           "http://172.16.5.70/pub/fssbxx/sbzx/tzgg/201209/t20120924_4070844.html",
                           "http://www.fsjy.net/fsjy/gg/tz/201209/t20120904_60453.html",
                           "http://172.16.5.70/pub/fssbxx/zwgk/zcfg/zcfg/zcfgyilbx/201208/t20120828_3881428.html",
                           "http://fswsjd.foshan.gov.cn/tzgg/201207/t20120727_3779183.html",
                           "http://fswsjd.foshan.gov.cn/tzgg/201207/t20120726_3778394.html",
                           "http://www.foshanepb.gov.cn/2012sjhjr/201205/t20120529_3579834.html",
                           "http://www.foshanepb.gov.cn/2012sjhjr/201205/t20120524_3557470.html",
                           ]

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