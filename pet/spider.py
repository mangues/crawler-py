# coding:utf-8
# 爬虫调度器
from pet import html_download,html_parser,url_manager,Outputer;

class Spider(object):
    def __init__(self):
        self.urls = url_manager.UrlManager();
        self.downLoader = html_download.HtmlDownLoad();
        self.parser = html_parser.HtmlParser();
        self.outputer = Outputer.Outputer();

    def craw(self,root_url):
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():   #如果有url
            try:
                new_url = self.urls.get_new_url()  #获取一个url
                print("解析:"+new_url)
                html = self.downLoader.download(new_url) #下载网页
                new_urls,new_data = self.parser.parse(new_url,html) #解析网页和所有待爬取url
                self.urls.add_new_urls(new_urls)  #加入到url管理器
                self.outputer.collect_data(new_data)  #输出器
            except Exception:
               print("解析错误:",Exception)

        self.outputer.out_html()


if __name__ == '__main__':
    spider = Spider()
    spider.craw("http://www.ichong123.com/")

