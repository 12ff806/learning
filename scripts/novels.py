#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__doc__ = "下载小说 需要认证token"


import os
import csv
import requests
from multiprocessing import Process


class Novel(object):
    """小说"""

    def __init__(self, id, title):
        self._id = id
        self._title = title
        
    @property
    def title(self):
        return self._title

    @property
    def info_url(self):
        """返回小说信息url"""
        info_url = "https://c75393.818tu.com/v1/novels/" + str(self._id)
        return info_url

    def content_url(self, chapter_id):
        """返回章节内容url
        :param chapter_id: 章节id
        """
        content_url = "https://c75393.818tu.com/v1/read/" + str(chapter_id)
        return content_url

    def get_last_n_chapter(self, n):
        """获取最新的n个章节数及章节id
        :param n: 要获取的最新章节数量

        :return: 返回列表 包含最新的n个章节数及id
        """
        info_resp = requests.get(self.info_url)
        info_json = info_resp.json()
        article_count = info_json["data"]["article_count"]

        chapter_url = self.info_url + "/catalog?start={}&limit={}".format(article_count-n, n)
        chapter_resp = requests.get(chapter_url)
        chapter_json = chapter_resp.json()
        
        return chapter_json["data"]

    def download(self, chapter_list, savedir="./"):
        """下载章节
        :param chapter_list: 包含章节信息的列表
        """
        headers = {"Authorization": "put your token here"}

        already_list = []
        if "log.csv" in os.listdir(savedir):
            with open(savedir + "log.csv", "r") as f:
                for line in f.readlines():
                    line = line.strip("\n")
                    already_list.append(line)

        new_list = [c for c in chapter_list if str(c["id"]) not in already_list]
        if not new_list:
            print(self.title + "没有更新")
        for chapter in new_list:
            resp = requests.get(self.content_url(chapter["id"]), headers=headers)
            data = resp.json()["data"]
            title = self.title + "_" + \
                    data["title"].split(" ")[0] + \
                    "_" + \
                    data["title"].split(" ")[1]
            content = data["content"]

            with open(savedir + title, "w") as f:
                f.write(content)

            with open(savedir + "log.csv", "a+") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=["id"])
                writer.writerow({"id": chapter["id"]})


if __name__ == "__main__":
    novels = [Novel(907, "神级龙卫"), Novel(14916, "最佳女婿"), Novel(15758, "财运天降")]
    for novel in novels:
        novel.download(novel.get_last_n_chapter(5), "/Users/sin/Desktop/novels/")

