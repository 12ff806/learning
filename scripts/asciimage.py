#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# by Sin <12ff806@protonmain.com>
# Aug 17 2017

"""转换 RGB 图片至字符图片
"""

from PIL import Image
import argparse
import sys


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("in_file_name")
    parser.add_argument("-o", "--output", type = str, default = "output.txt")
    parser.add_argument("--width", type = int, default = 80)
    parser.add_argument("--height", type = int, default = 50)

    args = parser.parse_args()
    in_file_name = args.in_file_name
    out_file_name = args.output
    width = args.width
    height = args.height
    
    return in_file_name, out_file_name, width, height


def get_char_from_rgb(r, g, b, alpha = 255):
    """
    将 rgb 转换为 0-255 的灰度值
    再将这 256 个灰度值映射到 ascii_char 字符上

    param:
        r: red值(0-255)
        g: green值(0-255)
        b: blue值(0-255)
        alpha: 不透明度(0-255)
    return:
        ascii_char 中的某个字符
    """
    
    # alpha == 0 完全透明 返回空格
    if alpha == 0:
        return " "
    # 定义 71 个 ascii 字符
    ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    length = len(ascii_char)
    # rgb 转换为灰度值 灰度值越大越接近白色 越小越接近黑色
    gray = int((2126 * r + 7152 * g + 722 * b) / 10000)
    x = int((gray / 256) * length)
    return ascii_char[x]


def get_char_from_gray(gray):
    ascii_char = list(" .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$")
    length = len(ascii_char)
    x = int((gray / 256) * length)
    return ascii_char[x]


def convert_to_asciimage(in_file_name, out_file_name, width = 80, height = 50):
    """
    将RGB图片转换为字符图片
    """
    image = Image.open(in_file_name)
    image = image.resize((width, height), Image.NEAREST)
    asciimage = ""
    for i in range(height):
        for j in range(width):
            rgba = image.getpixel((j, i))
            # 判断是否为灰度图
            if isinstance(rgba, int):
                asciimage += get_char_from_gray(rgba)
            # 默认为 RGB 图
            else:
                try:
                    asciimage += get_char_from_rgb(*rgba)
                except TypeError as e:
                    print("不是RGB图片 我也很绝望啊")
                    sys.exit(1)
        asciimage += "\n"
    print(asciimage)

    with open(out_file_name, "w") as f:
        f.write(asciimage)


if __name__ == "__main__":
    in_file_name, out_file_name, width, height = get_args()
    convert_to_asciimage(in_file_name, out_file_name, width, height)


