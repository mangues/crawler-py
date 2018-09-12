# coding:utf-8
# html 解析器
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup
class HtmlParser(object):
    def __init__(self):
        self.compile_href = ""

    def parse(self, url, html_str):
        if url is None or html_str is None:
            return None
        soup = BeautifulSoup(html_str,"html.parser",from_encoding="utf-8")
        new_urls = self._get_new_urls(url,soup)
        new_data = self._get_new_data(url,soup)
        return new_urls,new_data;

    def _get_new_urls(self, url, soup):
        new_urls = set()
        links = soup.find_all('a',href=self.compile_href)
        for link in links:
            new_url = link['href']
            new_urls.add(new_url)
        return new_urls

    def _get_new_data(self, url, soup):
        return None;