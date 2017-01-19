import requests

class HtmlDownloader(object):
    def download(self, url):

        if url is None:
            return None
        headers = {
            'Accept-Language': 'zh-cn',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/4.0 (compatible MSIE 6.00 Windows NT 5.1 SV1)',
        }

        res = requests.get(url, headers=headers)

        res.encoding = 'utf-8'

        return res.text
