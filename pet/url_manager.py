# coding:utf-8
# url 管理器
from pet.db.redisdb import RedisPool
from pet.conf.setting import redis_host,redis_password,redis_port,redis_db
class UrlManager(object):
    def __init__(self):
        self.redisPool = RedisPool(redis_host,redis_port,redis_password,redis_db)

    #增加新的url
    def add_new_url(self, url):
        if url is None:
            return
        if self.redisPool.isExistNew(url)==False and self.redisPool.isExistOld(url)==False:
            self.redisPool.putNew(url)
        pass

    #判断是否有url
    def has_new_url(self):
        return self.redisPool.isExistInNew()

    #获取最新的url并加入已使用
    def get_new_url(self):
        url = self.redisPool.getNew()
        self.redisPool.putOld(url)
        return url

    #批量加入url
    def add_new_urls(self, new_urls):
        if new_urls is None or len(new_urls) == 0:
            return
        for url in new_urls:
            self.redisPool.putNew(url)
