# coding:utf-8
# html 解析器
import re
from pet.parser.html_parser import HtmlParser
class IchongParser(HtmlParser):
    def __init__(self):
        self.compile_href = re.compile(r"http://www.ichong123.com/[^\s]*")

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