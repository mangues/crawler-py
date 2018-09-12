import redis

class RedisPool(object):
    rdp=None;
    baseKey = "crawler"
    newKey = baseKey+":new"
    oldKey = baseKey+":old"
    def __init__(self,host,port,password,db):
        if password == None:
            self.rdp = redis.ConnectionPool(host=host, port=port,db=db)
        else:
            self.rdp = redis.ConnectionPool(host=host, port=port,password = password,db=db)
        self.rdc = redis.StrictRedis(connection_pool=self.rdp)


    def putNew(self,key):
        self.rdc.sadd(self.newKey, key)


    def putOld(self, key):
        self.rdc.sadd(self.oldKey , key)

    #new set 中是否存在数据
    def isExistInNew(self):
        scard = self.rdc.scard(self.newKey)
        if scard !=0:
            return True
        else:
            return False

    #获得一个newset数据并移除
    def getNew(self):
        randomkey = self.rdc.spop(self.newKey)
        return str(randomkey,"utf8")

    #new set中是否存在
    def isExistNew(self,key):
        return self.__isExist(self.newKey, key)

    #old set中是否存在
    def isExistOld(self, key):
        return self.__isExist(self.oldKey,key)

    # 把key 从new 移动到old
    def moveNew2old(self,key):
        self.rdc.smove(self.newKey,self.oldKey,key)




    def __isExist(self, name,key):
        sismember = self.rdc.sismember(name, key)
        return sismember









