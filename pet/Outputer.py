# -*- coding: utf-8 -*-
# 输出器
class Outputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    def out_html(self):
        fout = open("out.html","w")
        fout.write("<html>")
        for data in self.datas:
            # fout.write(str(data["title"]))
            # fout.write("<br>")
            # fout.write(str(data["content"]))
            print(data["title"])
        fout.write("</html>")

