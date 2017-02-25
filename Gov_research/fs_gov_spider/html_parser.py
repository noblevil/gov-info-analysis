#!/usr/bin/env python
# _*_ encoding:utf-8 _*_

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
from utils import myjoin

class HtmlParser(object):
    def _get_news_urls(self, soup):
        news_urls = []
        links = soup.find_all('a', href=re.compile(r'/\d+/\w+\.html'))
        for link in links:
            news_url = link['href']
            news_full_url = myjoin("http://www.foshan.gov.cn/zwgk/gggs/", news_url)
            news_urls.append(news_full_url)
        return news_urls


    def _get_new_data(self, page_url, soup):
        res_data = {}

        #公告URL
        res_data['url'] = page_url

        #公告标题
        res_data['title'] = soup.select('.content_title')[0].text

        #公告来源
        res_data['source'] = soup.select('.content_mess  span label')[0].test

        #公告发布时间
        timesource = soup.select('.content_mess  span label')[1].text
        res_data['time'] = datetime.strptime(timesource, '%Y.%m.%d')

        #公告内容
        res_data['content'] = soup.select("#content_box")[0].text

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




