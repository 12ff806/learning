#!/usr/bin/env python3


__doc__ = "每天短信提醒我是否购买彩票, 以及购买什么号码"
__author__ = "12ff806"


import urllib.request
import urllib.error
import re
import os
import time


class Reminder(object):
    """
    抓取3D福彩开奖结果, 分析后短信提醒我是否购买
    """
    def __init__(self):
        # 基础url
        self._base_url = ["http://kaijiang.zhcw.com/zhcw/html/3d/list_", "http://kaijiang.zhcw.com/zhcw/inc/3d/3d_wqhg.jsp?pageNum="]

        # 保存首页页面的源码
        self._web_source = ""

        # 保存最近20期中奖号码
        self._result = None

    def get_web_source(self):
        """
        获取首页20期的页面源码
        """
        try:
            url = self._base_url[0] + str(1) + ".html"
            request = urllib.request.urlopen(url)
        except urllib.error.HTTPError as e:
            print("error, try another url..")
            url = self._base_url[1] + str(1)
            request = urllib.request.urlopen(url)
            
        print("request url: {0}".format(url))
        self._web_source = request.read().decode("utf-8")
        #print(self._web_source)

    def clean(self):
        """
        从源码中清洗出数据
        """
        reg = re.compile('<tr>.*?<td align="center">(.*?)</td>.*?<td align="center">(.*?)</td>.*?<td align="center" style="padding-left:20px;"><em>(.*?)</em>.*?<em>(.*?)</em>.*?<em>(.*?)</em></td>', re.S)
        self._result = re.findall(reg, self._web_source)
        print(self._result)

    def calc(self):
        """
        分析当前数据, 给出购买建议
        """
        # 按4推1的方式给出购买建议
        num_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
        s = set()
        for i in range(2, 5):
            s.add(int(self._result[3][i]))
            s.add(int(self._result[2][i]))
            s.add(int(self._result[1][i]))
            s.add(int(self._result[0][i]))
        
        diff_set = num_set - s
        msg = time.ctime() + "/ " + "当前获取到的期数为: " + self._result[0][0] + "/ " + "按四推一的方式得出: " + str(diff_set) + " 没有出现"
        if len(diff_set) == 2:
            msg = msg + "/ " + "建议购买: " + str(diff_set) + "复式"
        
        # 发送短信
        pass
        # 保存日志
        with open("./reminder_log", "a+") as f:
            f.write(msg)
            f.write("\r\n")


if __name__ == "__main__":
    r = Reminder()
    r.get_web_source()
    r.clean()
    r.calc()

