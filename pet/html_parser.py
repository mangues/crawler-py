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
        crumbs_node = soup.find("ul", class_="crumbs-bar")
        ac_content_node = soup.find("div", class_="article-content")
        if crumbs_node==None or ac_content_node==None:
            return
        res_data = {}
        tag_bar = []
        find_all = crumbs_node.find_all("li")
        for tag in find_all:
            find = tag.find("a")
            if find !=None:
                text = find.get_text()
                if text!="宠物网":
                    tag_bar.append(text)


        title_node = ac_content_node.find("h1", class_="ac-title")
        res_data["title"] =title_node.get_text()
        content_node = ac_content_node.find("div", class_="ac-content").find("table")
        res_data["summary"] = content_node.get_text()
        res_data["content"] = str(content_node)
        res_data["url"] = url
        res_data["tags"] = tag_bar
        return res_data;