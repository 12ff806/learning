#!/usr/bin/env python3



import urllib.request
import urllib.error
import csv
import re
import os
import time


class Grab(object):
    """
    抓取3D福彩开奖结果
    """
    def __init__(self):
        # 基础url
        self._base_url = ["http://kaijiang.zhcw.com/zhcw/html/3d/list_", "http://kaijiang.zhcw.com/zhcw/inc/3d/3d_wqhg.jsp?pageNum="]

        # 总共抓取250页的内容
        self._page_num = 250

        # 保存所有页面的源码
        self._web_source = ""

        # 临时结果
        self._result = None

        # 保存到文件
        self._save_fn = "3d_lottery.csv"

        # csv文件列名
        #self._fieldname = ["日期", "期号", "中奖号码-百位", "中奖号码-十位", "中奖号码-个位"]
        self._fieldname = ["Date", "PeriodNum", "HDigit", "TDigit", "Digit"]

    def get_web_source(self):
        """
        获取页面源码
        """
        for index in range(1, self._page_num+1):
            url = None
            request = None

            try:
                url = self._base_url[0] + str(index) + ".html"
                request = urllib.request.urlopen(url)
            except urllib.error.HTTPError as e:
                print("error, try another url..")
                url = self._base_url[1] + str(index)
                request = urllib.request.urlopen(url)
            
            print("request url: {0}".format(url))
            html = request.read().decode("utf-8")
            self._web_source = self._web_source + html
        #print(self._web_source)
        #return web_source

    def clean(self):
        """
        从源码中清洗出数据
        """
        reg = re.compile('<tr>.*?<td align="center">(.*?)</td>.*?<td align="center">(.*?)</td>.*?<td align="center" style="padding-left:20px;"><em>(.*?)</em>.*?<em>(.*?)</em>.*?<em>(.*?)</em></td>', re.S)
        self._result = re.findall(reg, self._web_source)
        #print(self._result)

    def save(self):
        """
        将中奖数据保存到文件
        """
        # 当前目录下是否存在"data"目录, 不存在则创建
        cdl = [d for d in os.listdir(".") if os.path.isdir(d)]
        if "data" not in cdl:
            os.mkdir(os.path.join(os.path.abspath("."), "data"))
        
        # 判断是否存在, 存在则重命名
        if self._save_fn in os.listdir(os.path.join(os.path.abspath("."), "data")):
            os.rename("./data/"+self._save_fn, "./data/3d_lottery_"+str(time.time()).split(".")[0]+".csv")
        
        # 写入csv
        with open("./data/"+self._save_fn, "a+") as csvfile:
            # 写头信息
            writer = csv.DictWriter(csvfile, fieldnames=self._fieldname)
            writer.writeheader()
            
            # 写数据
            while True:
                record_dict = {}
                try:
                    record = self._result.pop()
                    record_dict["Date"] = record[0]
                    record_dict["PeriodNum"] = record[1]
                    record_dict["HDigit"] = record[2]
                    record_dict["TDigit"] = record[3]
                    record_dict["Digit"] = record[4]
                    
                    writer.writerow(record_dict)
                except IndexError as e:
                    break
                    

if __name__ == "__main__":
    g = Grab()
    g.get_web_source()
    g.clean()
    g.save()

