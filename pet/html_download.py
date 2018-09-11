# coding:utf-8
import urllib.request as urllib

# 页面下载器
class HtmlDownLoad(object):
    def download(self, url):
        if url is None:
            return None
        response = urllib.urlopen(url)
        if response.getcode() != 200:
            return  None
        return response.read()