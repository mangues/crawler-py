# coding:utf-8
# 工厂
import re
from pet.parser.ichong_parser import IchongParser
from pet.parser.yc_parser import YCParser
compile_href = re.compile(r"http://www.ichong123.com/[^\s]*")
yc_compile_href = re.compile(r"http://www.yc.cn/[^\s]*")
ichong_parser = IchongParser()
yc_arser = YCParser()
class ParserFactory(object):
    @staticmethod
    def get_parser(url):
        if compile_href.match(url):
            return ichong_parser;
        if yc_compile_href.match(url):
            return yc_arser;





