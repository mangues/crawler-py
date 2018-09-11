# coding:utf-8
# url 管理器
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    #增加新的url
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
        pass

    #判断是否有url
    def has_new_url(self):
        return len(self.new_urls) != 0;

    #获取最新的url并加入已使用
    def get_new_url(self):
        url = self.new_urls.pop()
        self.old_urls.add(url)
        return url

    #批量加入url
    def add_new_urls(self, new_urls):
        if new_urls is None or len(new_urls) == 0:
            return
        for url in new_urls:
            self.add_new_url(url)
