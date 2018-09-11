# coding:utf-8
# html 解析器
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup

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
        links = soup.find_all('a',href=re.compile(r"/item/[^\s]*"))
        for link in links:
            new_url = link['href']
            new_full_url = "https://baike.baidu.com"+new_url
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, url, soup):
        res_data = {}
        title_node = soup.find("dd", class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data["title"] =title_node.get_text()
        content_node = soup.find("div", class_="lemma-summary").find("div")
        res_data["content"] = content_node.get_text()
        res_data["url"] = url
        return res_data;