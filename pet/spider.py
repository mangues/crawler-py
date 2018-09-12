# coding:utf-8
# 爬虫调度器
from pet import html_download,html_parser,url_manager,outputer;
from threading import Thread

class Spider(object):
    def __init__(self):

        self.urls = url_manager.UrlManager();
        self.downLoader = html_download.HtmlDownLoad();
        self.parser = html_parser.HtmlParser();
        self.outputer = outputer.Outputer();

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
            except Exception as e:
               print("解析错误:",e)


class CrawThread(Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        print('%s 线程启动' % self.name)
        spider = Spider()
        spider.craw("http://www.ichong123.com/")

if __name__ == '__main__':
    crawThread1 = CrawThread('1号')
    crawThread2 = CrawThread('2号')
    crawThread3 = CrawThread('3号')
    crawThread4 = CrawThread('4号')
    crawThread1.start()
    crawThread2.start()
    crawThread3.start()
    crawThread4.start()

