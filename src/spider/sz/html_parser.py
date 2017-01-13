from bs4 import BeautifulSoup
from datetime import datetime
import re
import urllib

class HtmlParser(object):

    def _get_news_urls(self, soup):
        news_urls = []
        links = soup.find_all('a', href=re.compile(r'/\d+/\w+\.htm'))
        for link in links:
            news_url = link['href']
            news_full_url = urllib.parse.urljoin("http://www.sz.gov.cn/cn/xxgk/zfxxgj/tzgg/",news_url)
            news_urls.append(news_full_url)
        return news_urls


    def _get_new_data(self, page_url, soup):
        res_data = {}

        #公告URL
        res_data['url'] = page_url

        #公告标题
        res_data['title'] = soup.select('.tit h1')[0].text

        #公告来源
        res_data['source'] = soup.select('.tit span')[0].text

        #公告发布时间
        timesource = soup.select('.tit span')[1].text.rstrip("信息提供日期：")
        res_data['time'] = timesource #datetime.strptime(timesource, '%Y-%m-%d')

        #公告内容
        report_text = soup.find_all('p')
        text = ''
        for p in report_text:
            text += p.get_text()
            text += '\n'
        res_data['content'] = text

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




