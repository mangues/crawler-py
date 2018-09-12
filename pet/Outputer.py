# -*- coding: utf-8 -*-
# 输出器
from pet.db.mongodb import mongodb
class Outputer(object):
    def __init__(self):
        self.datas = []
        self.mongodb = mongodb()

    def collect_data(self,data):
        if data is None:
            return
        self.mongodb.insetItem(data)
        self.datas.append(data)



