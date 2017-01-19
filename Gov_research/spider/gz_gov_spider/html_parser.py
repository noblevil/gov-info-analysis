import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import urllib

class HtmlParser(object):
    def _get_news_urls(self, soup):
        news_urls = []
        links = soup.find_all('a', href=re.compile(r'/gzgov/gsgg/\d+/\w+\.shtml'))
        for link in links:
            news_url = link['href']
            news_full_url = urllib.parse.urljoin("http://www.gz.gov.cn", news_url)
            news_urls.append(news_full_url)
        return news_urls


    def _get_new_data(self, page_url, soup):
        res_data = {}

        #公告URL
        res_data['url'] = page_url

        #公告标题
        res_data['title'] = soup.select('.info_title')[0].text

        #公告来源
        res_data['source'] = soup.select('.ly')[0].text

        #公告发布时间
        timesource = soup.select('.time')[0].text.strip()
        res_data['time'] = datetime.strptime(timesource, '%Y-%m-%d %H:%M:%S')

        #公告内容
        res_data['content'] = soup.select("#zoomcon")[0].text.strip()

        #公告浏览次数
        views_url = "http://www.gz.gov.cn/sofpro/gzyyqt/info_count/info_count3.jsp?url=" + page_url
        views = requests.get(views_url)
        res_data['views'] = views.text.strip()

        return res_data

    def paser_data(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_data = self._get_new_data(page_url, soup)
        return new_data

    def paser_page_urls(self, html_cont):
        if  html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        news_urls = self._get_news_urls(soup)
        return news_urls




