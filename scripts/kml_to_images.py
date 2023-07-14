#!/usr/bin/env python3


import re
import requests


def coord_extract(coord_str):
    """ 提取坐标字符串
    """
    try:
        return ",".join(coord_str.split(" ")[0:2])
    except Exception as e:
        return None


def time_extract(time_str):
    """ 提取时间
    """
    try:
        pass
    except Exception as e:
        return None
    

def read_kml(kml_file=None):
    """ 读取 kml 文件里的 轨迹坐标列表 和 时间列表
    """
    try:
        if not kml_file:
            return None

        kml_str = ""
        with open(kml_file) as f:
            kml_str = f.read()

        if not kml_str:
            return None
        
        # 轨迹坐标列表
        coord_list = re.findall("<gx:coord>(.*)</gx:coord>", str)
        # 时间列表 这里的时间是UTC时间
        time_list = re.findall("<when>(.*)</when>", str)

        if len(coord_list) != len(time_list):
            return None

        return coord_list, time_list
    except Exception as e:
        return None


def get_map_img_by_coord(coord_str):
    """ 通过坐标获取地图矢量图
    """
    try:
        # 天地图key
        token = "e429c9f1fb0420bd07eb0b26129fdfea"
        url_schema = "http://api.tianditu.gov.cn/staticimage?center={}&width=1024&height=1024&zoom=16&layers=vec_c,cva_c&tk={}"
        url = url_schema.format(coord_str, token)
        
        # 请求数据
        s = requests.Session()
        resp = s.get(url)
        pass
    except Exception as e:
        return None


