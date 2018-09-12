# coding:utf-8
import pymongo
from pet.conf.setting import mongo_host,mongo_port,mongo_user,mongo_psw,mongo_db_name,mongo_db_collection
class mongodb(object):
    def __init__(self):
        host = mongo_host
        port = mongo_port
        user = mongo_user
        psw  =  mongo_psw
        collection  =  mongo_db_collection
        dbname  =  mongo_db_name
        client = pymongo.MongoClient(host=host,port=port)
        db = client[dbname]
        db.authenticate(user, psw)
        self.post = db[collection]

    def insetItem(self,data):
        self.post.insert(data)
