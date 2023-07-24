#!/usr/bin/env python3


import re
import requests
from PIL import Image, ImageFont, ImageDraw, ImageFile
from io import BytesIO
import datetime
import argparse
import os


ImageFile.LOAD_TRUNCATED_IMAGES = True


def get_args():
    """ 获取程序输入参数
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--kmlfile", type = str, default = "test.kml")
    
    args = parser.parse_args()
    kml_file = args.kmlfile
    
    return kml_file


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
        new_time_str = time_str.replace("T", " ").replace("Z", "")
        date_time = datetime.datetime.strptime(new_time_str, "%Y-%m-%d %H:%M:%S")
        new_date_time = date_time + datetime.timedelta(hours=8)
        new_date_time_str = str(new_date_time)
        return new_date_time_str
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
        coord_list = re.findall("<gx:coord>(.*)</gx:coord>", kml_str)
        # 时间列表 这里的时间是UTC时间
        time_list = re.findall("<when>(.*)</when>", kml_str)

        if len(coord_list) != len(time_list):
            return None

        return coord_list, time_list
    except Exception as e:
        return None


def get_map_img_by_coord(coord_str, save_name):
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
        i = Image.open(BytesIO(resp.content))
        i.save(save_name)
    except Exception as e:
        return None


def get_img_location(center_coord, pix_location):
    """ 获取相对位置的屏幕标注坐标
    """
    try:
        # 天地图key
        token = "e429c9f1fb0420bd07eb0b26129fdfea"
        url_schema = "http://api.tianditu.gov.cn/staticimage?center={}&width=1024&height=1024&zoom=16&layers=vec_c,cva_c&pixLocation={}&tk={}"
        url = url_schema.format(center_coord, pix_location, token)
        
        # 请求数据
        s = requests.Session()
        resp = s.get(url)
        return resp.text
    except Exception as e:
        return None


def draw_img(img_name, coord_str, time_str, location_str):
    """ 画图
    """
    try:
        img = Image.open(img_name)
        
        img_dr = ImageDraw.Draw(img)
        
        # 画时间
        font = ImageFont.truetype('/usr/share/fonts/noto/NotoSansMono-Regular.ttf', 30)
        img_dr.text((5, 989), time_str, font=font, fill=(255,0,0))

        # 画线
        if location_str:
            location_list = location_str.split("||")
            location_list = list(reversed(location_list))
            pre_location = "512,512"
            for loc in location_list:
                pre_loc_x, pre_loc_y = pre_location.split(",")
                loc_x, loc_y = loc.split(",")
                img_dr.line((pre_loc_x, pre_loc_y, loc_x, loc_y), fill=(0, 0, 255), width=5)
                pre_location = loc

        img_dr.ellipse((505, 505, 519, 519), fill=(255,0,0), outline=(255,0,0), width=2)
        img.save(img_name, quality=100)
    except Exception as e:
        print(e)


def run(kml_file):
    try:
        # 获取 坐标 和 时间 列表
        coord_list, time_list = read_kml(kml_file)
        
        # 遍历 坐标 和 时间 列表
        for i in range(len(coord_list)):
            coord_str = coord_list[i]
            time_str = time_list[i]

            # 获取坐标 和 时间
            coord_str = coord_extract(coord_str)
            time_str = time_extract(time_str)

            # 获取地图矢量图
            save_path = "kml_imgs"
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            save_name = save_path + "/" + str(i+1) + ".png"
            get_map_img_by_coord(coord_str, save_name)

            # 获取当前坐标前20个坐标 和 坐标 在图片中的相对位置
            pix_coord_list = []
            pix_list = coord_list[i-20: i] or \
                       coord_list[i-19: i] or \
                       coord_list[i-18: i] or \
                       coord_list[i-17: i] or \
                       coord_list[i-16: i] or \
                       coord_list[i-15: i] or \
                       coord_list[i-14: i] or \
                       coord_list[i-13: i] or \
                       coord_list[i-12: i] or \
                       coord_list[i-11: i] or \
                       coord_list[i-10: i] or \
                       coord_list[i-9: i] or \
                       coord_list[i-8: i] or \
                       coord_list[i-7: i] or \
                       coord_list[i-6: i] or \
                       coord_list[i-5: i] or \
                       coord_list[i-4: i] or \
                       coord_list[i-3: i] or \
                       coord_list[i-2: i] or \
                       coord_list[i-1: i]
            for pix in pix_list:
                pix_coord = coord_extract(pix)
                pix_coord_list.append(pix_coord)

            pix_location = ""
            if pix_coord_list:
                pix_location = "|".join(pix_coord_list)

            # 获取坐标在图片中的相对位置
            location_str = ""
            if pix_location:
                location_str = get_img_location(coord_str, pix_location)
            
            # 画图
            draw_img(save_name, coord_str, time_str, location_str)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    #coord_str = "116.414392,39.946199"
    #save_name = "test.png"
    #get_map_img_by_coord(coord_str, save_name)

    #center_coord = "116.414392,39.946199"
    #pix_location = "116.414392,39.946199|116.414392,39.946199"
    #print(get_img_location(center_coord, pix_location))

    kml_file = get_args()
    run(kml_file)

