# coding:utf-8
# html 解析器
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup
compile_news = re.compile(u'http://www.ichong123.com/news/[^\s]*')
compile_href = re.compile(r"http://www.ichong123.com/[^\s]*")
class HtmlParser(object):
    def parse(self, url, html_str):
        if url is None or html_str is None:
            return None
        soup = BeautifulSoup(html_str,"html.parser",from_encoding="utf-8")
        new_urls = self._get_new_urls(url,soup)
        new_data = self._get_new_data(url,soup)
        return new_urls,new_data;

    def _get_new_urls(self, url, soup):
        new_urls = set()
        links = soup.find_all('a',href=compile_href)
        for link in links:
            new_url = link['href']
            new_urls.add(new_url)
        return new_urls

    def _get_new_data(self, url, soup):
        matchObj = re.match(compile_news,url)
        if matchObj is None:
            return

        res_data = {}
        title_node = soup.find("h1", class_="ac-title")
        res_data["title"] =title_node.get_text()
        content_node = soup.find("div", class_="ac-content").find("table")
        res_data["summary"] = content_node.get_text()
        res_data["content"] = str(content_node)
        res_data["url"] = url
        return res_data;