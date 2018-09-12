# coding:utf-8
# 爬虫调度器
from pet import html_download,url_manager,outputer;
from pet.parser.parser_factory import ParserFactory;
from threading import Thread

class Spider(object):
    def __init__(self):
        self.urls = url_manager.UrlManager();
        self.downLoader = html_download.HtmlDownLoad();
        self.outputer = outputer.Outputer();

    def craw(self):
        while self.urls.has_new_url():   #如果有url
            try:
                new_url = self.urls.get_new_url()  #获取一个url
                print("解析:"+new_url)
                html = self.downLoader.download(new_url) #下载网页
                parser = ParserFactory.get_parser(new_url)
                new_urls,new_data = parser.parse(new_url,html) #解析网页和所有待爬取url
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
        spider.urls.add_new_url("http://www.ichong123.com/")
        spider.urls.add_new_url("http://www.yc.cn/news/")
        spider.craw()

if __name__ == '__main__':
    crawThread1 = CrawThread('1号')
    # crawThread2 = CrawThread('2号')
    # crawThread3 = CrawThread('3号')
    # crawThread4 = CrawThread('4号')
    # crawThread5 = CrawThread('5号')
    # crawThread6 = CrawThread('6号')
    # crawThread7 = CrawThread('7号')
    # crawThread8 = CrawThread('8号')
    # crawThread9 = CrawThread('9号')
    # crawThread10 = CrawThread('10号')
    # crawThread11 = CrawThread('11号')
    crawThread1.start()
    # crawThread2.start()
    # crawThread3.start()
    # crawThread4.start()
    # crawThread5.start()
    # crawThread6.start()
    # crawThread7.start()
    # crawThread8.start()
    # crawThread9.start()
    # crawThread10.start()
    # crawThread11.start()

