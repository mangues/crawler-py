# coding:utf-8
# 有宠html 解析器
import re
from bs4 import BeautifulSoup
from pet.parser.html_parser import HtmlParser
class YCParser(HtmlParser):
    def __init__(self):
        self.compile_href = re.compile(r"http://www.yc.cn/[^\s]*")

    def _get_new_data(self, url, soup):
        ac_content_node = soup.find("div", class_="news-detail")
        if  ac_content_node==None:
            return
        res_data = {}

        title_node = ac_content_node.find("div", class_="title-box").find("h1",class_="title")
        res_data["title"] =title_node.get_text()
        content_node = ac_content_node.find("div", class_="info-box")
        res_data["summary"] = content_node.get_text()
        res_data["content"] = str(content_node)
        res_data["url"] = url
        return res_data;