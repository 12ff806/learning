#!/usr/bin/env python3


import re
import requests
from PIL import Image, ImageFont, ImageDraw, ImageFile
from io import BytesIO
import datetime
import argparse
import os
import math
import cv2
import glob


ImageFile.LOAD_TRUNCATED_IMAGES = True


# amap key
token = "ce09d1af923103ad333c59693e6e434d"


class LngLatTransfer():
    """ 坐标转换 天地图坐标系WGS84 高德地图坐标系GCJ02
    两步路的坐标为WGS84 使用高德地图则需要转换为GCJ02
    """
    def __init__(self):
        self.x_pi = 3.14159265358979324 * 3000.0 / 180.0
        self.pi = math.pi  # π
        self.a = 6378245.0  # 长半轴
        self.es = 0.00669342162296594323  # 偏心率平方

    def WGS84_to_GCJ02(self, lng, lat):
        '''
        实现WGS84坐标系向GCJ02坐标系的转换
        :param lng: WGS84坐标系下的经度
        :param lat: WGS84坐标系下的纬度
        :return: 转换后的GCJ02下经纬度
        '''
        dlat = self._transformlat(lng - 105.0, lat - 35.0)
        dlng = self._transformlng(lng - 105.0, lat - 35.0)
        radlat = lat / 180.0 * self.pi
        magic = math.sin(radlat)
        magic = 1 - self.es * magic * magic
        sqrtmagic = math.sqrt(magic)
        dlat = (dlat * 180.0) / ((self.a * (1 - self.es)) / (magic * sqrtmagic) * self.pi)
        dlng = (dlng * 180.0) / (self.a / sqrtmagic * math.cos(radlat) * self.pi)
        gcj_lng = lng + dlng
        gcj_lat = lat + dlat
        return round(gcj_lng, 6), round(gcj_lat, 6)

    def _transformlat(self, lng, lat):
        ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + \
              0.1 * lng * lat + 0.2 * math.sqrt(math.fabs(lng))
        ret += (20.0 * math.sin(6.0 * lng * self.pi) + 20.0 *
                math.sin(2.0 * lng * self.pi)) * 2.0 / 3.0
        ret += (20.0 * math.sin(lat * self.pi) + 40.0 *
                math.sin(lat / 3.0 * self.pi)) * 2.0 / 3.0
        ret += (160.0 * math.sin(lat / 12.0 * self.pi) + 320 *
                math.sin(lat * self.pi / 30.0)) * 2.0 / 3.0
        return ret

    def _transformlng(self, lng, lat):
        ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + \
              0.1 * lng * lat + 0.1 * math.sqrt(math.fabs(lng))
        ret += (20.0 * math.sin(6.0 * lng * self.pi) + 20.0 *
                math.sin(2.0 * lng * self.pi)) * 2.0 / 3.0
        ret += (20.0 * math.sin(lng * self.pi) + 40.0 *
                math.sin(lng / 3.0 * self.pi)) * 2.0 / 3.0
        ret += (150.0 * math.sin(lng / 12.0 * self.pi) + 300.0 *
                math.sin(lng / 30.0 * self.pi)) * 2.0 / 3.0
        return ret


def get_args():
    """ 获取程序输入参数
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--kmlfile", type = str, default = "test.kml")
    parser.add_argument("-v", "--video", type = str, default = "")
    
    args = parser.parse_args()
    kml_file = args.kmlfile
    video = args.video
    
    return kml_file, video


#def coord_extract(coord_str):
#    """ 提取坐标字符串
#    """
#    try:
#        return ",".join(coord_str.split(" ")[0:2])
#    except Exception as e:
#        return None


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


def get_map_img_by_coord(coord_str, save_name, pix_list):
    """ 通过坐标获取地图矢量图
    """
    try:
        url_schema = ""
        url = ""
        if not pix_list:
            url_schema = "https://restapi.amap.com/v3/staticmap?location={}&zoom=15&size=1024*576&scale=1&key={}"
            url = url_schema.format(coord_str, token)
        else:
            url_schema = "https://restapi.amap.com/v3/staticmap?location={}&zoom=15&size=1024*576&scale=1&paths={}&key={}"
            pix_shcema = "4,0x0000ff,1,,:{}"
            
            pix1 = pix_list[0:4]
            pix2 = pix_list[3:7]
            pix3 = pix_list[6:10]
            
            paths_list = []
            if pix1:
                pix1_str = ";".join(pix1)
                paths_list.append(pix_shcema.format(pix1_str))
            if pix2:
                pix2_str = ";".join(pix2)
                paths_list.append(pix_shcema.format(pix2_str))
            if pix3:
                pix3_str = ";".join(pix3)
                paths_list.append(pix_shcema.format(pix3_str))
            paths_str = "|".join(paths_list)
                
            url = url_schema.format(coord_str, paths_str, token)
        
        # 请求数据
        s = requests.Session()
        resp = s.get(url)
        i = Image.open(BytesIO(resp.content))
        i.save(save_name)
    except Exception as e:
        return None


def draw_img(img_name, coord_str, time_str):
    """ 画图
    """
    try:
        img = Image.open(img_name)
        img = img.convert("RGBA")
        
        img_dr = ImageDraw.Draw(img)
        
        # 画时间
        font_time = ImageFont.truetype('/usr/share/fonts/noto/NotoSansMono-Regular.ttf', 18)
        img_dr.text((808, 547), time_str, font=font_time, fill=(255,0,0))

        # 画logo
        font_logo = ImageFont.truetype('/usr/share/fonts/adobe-source-han-sans/SourceHanSansCN-Bold.otf', 20)
        img_dr.text((911, 5), "虚无制造机", font=font_logo, fill=(255,0,0))
        
        # 画圆
        img_dr.ellipse((505, 281, 519, 295), fill=(255,0,0), outline=(255,0,0), width=1)
        img.save(img_name, quality=100)
    except Exception as e:
        print(e)


def images_to_video(img_path):
    """ 图片合成视频
    """
    try:
        frame_size = (1024, 576)
        out_video_name = img_path + "/" + "output_video.avi"
        out = cv2.VideoWriter(out_video_name ,cv2.VideoWriter_fourcc(*'DIVX'), 10, frame_size)

        img_list = glob.glob(img_path + "/*.png")

        #def natural_sort_key(s):
        #    """ 按文件名的结构排序 即依次比较文件名的非数字和数字部分
        #    """
        #    sub_strings = re.split(r"(\d+)", s)
        #    sub_strings = [int(c) if c.isdigit() else c for c in sub_strings]
        #    return sub_strings

        #img_list = sorted(img_list, key=natural_sort_key)
        img_list = sorted(img_list, key=lambda x: int(re.search("(\d+)", x).group()))
        
        for img_name in img_list:
            img = cv2.imread(img_name)
            out.write(img)

        out.release()
    except Exception as e:
        print(e)


def run(kml_file):
    try:
        # 获取 坐标 和 时间 列表
        coord_list_ori, time_list = read_kml(kml_file)
        #print(coord_list)
        #print(time_list)

        # 转换坐标
        coord_list = []
        llt = LngLatTransfer()
        for coord in coord_list_ori:
            coord_l = coord.split(" ")
            lng = float(coord_l[0])
            lat = float(coord_l[1])
            lng_new, lat_new = llt.WGS84_to_GCJ02(lng, lat)
            coord_list.append("{},{}".format(lng_new, lat_new))
        
        # 图片 视频 保存路径
        save_path = "kml_imgs"
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # 遍历 坐标 和 时间 列表
        for i in range(len(coord_list)):
            coord_str = coord_list[i]
            time_str = time_list[i]

            # 获取坐标 和 时间
            #coord_str = coord_extract(coord_str)
            time_str = time_extract(time_str)
            
            # 获取当前坐标前9个坐标 和 坐标 在图片中的相对位置
            pix_list = coord_list[i-9: i] or \
                       coord_list[i-8: i] or \
                       coord_list[i-7: i] or \
                       coord_list[i-6: i] or \
                       coord_list[i-5: i] or \
                       coord_list[i-4: i] or \
                       coord_list[i-3: i] or \
                       coord_list[i-2: i] or \
                       coord_list[i-1: i]
            if pix_list:
                pix_list.append(coord_str)

            # 获取地图矢量图
            save_name = save_path + "/" + str(i+1) + ".png"
            
            get_map_img_by_coord(coord_str, save_name, pix_list)

            # 画图
            try:
                draw_img(save_name, coord_str, time_str)
            except Exception as e:
                draw_img(save_name, coord_str, time_str)

            print(save_name)

        # 合成视频
        images_to_video(save_path)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    kml_file, video = get_args()
    if video:
        images_to_video(video)
    else:
        run(kml_file)

