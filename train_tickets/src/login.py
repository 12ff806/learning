#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Aug 01 2017
# by Sin


import urllib
import http.cookiejar
import ssl
import json
import re
import io
import gzip
import random
import datetime
import sys
from config import get_captcha_url, get_captcha_headers
from config import check_captcha_url, check_captcha_headers
from config import login_url, login_headers
from config import user_login_url, user_login_headers
from config import uamtk_url, uamtk_headers
from config import uamauthclient_url, uamauthclient_headers
from config import profile_url, profile_headers
    

# 阻止重定向
class NoRedirection(urllib.request.HTTPErrorProcessor):
    def http_response(self, request, response):
        return response
    
    https_response = http_response


# 判断是否已经登录
def is_login():
    # 创建 OpenerDirector 实例
    cookie = http.cookiejar.LWPCookieJar("cookie12306")
    cookie_handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(cookie_handler, NoRedirection)

    # 从文件加载 cookie
    try:
        cookie.load(ignore_discard=True)
    except FileNotFoundError:
        pass
    
    # 关闭 SSL 验证
    ssl._create_default_https_context = ssl._create_unverified_context

    # 构造 Request
    req = urllib.request.Request(profile_url, headers=profile_headers)

    # 发送打开个人中心请求
    profile_response = opener.open(req, timeout=5)
    if profile_response.status == 200:
        profile_response.close()
        return True
    else:
        profile_response.close()
        return False


# 登录处理
def login(username, password):
    # 1. 登录请求
    # 创建 OpenerDirector 实例
    cookie = http.cookiejar.LWPCookieJar("cookie12306")
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)

    # 从文件加载 cookie
    cookie.load(ignore_discard=True)

    # 构造 Request
    login_postdata = {
        "username": username,
        "password": password,
        "appid": "otn"
    }
    login_postdata = urllib.parse.urlencode(login_postdata).encode("utf-8")
    req = urllib.request.Request(login_url, login_postdata, login_headers)
    
    # 关闭 SSL 验证
    ssl._create_default_https_context = ssl._create_unverified_context

    # 发送登录请求
    login_response = opener.open(req, timeout=5)
    
    # 存储 cookie 到文件
    cookie.save(ignore_discard=True, ignore_expires=True)
    
    # 获取并解析 Response
    if login_response.info()["Content-Encoding"] == "gzip":
        buf = io.BytesIO(login_response.read())
        f = gzip.GzipFile(fileobj=buf)
        login_response_json = f.read().decode("utf-8")
        login_response_dict = json.loads(login_response_json)
        print(login_response_dict.get("result_message"))

    # 关闭请求
    login_response.close()
    
    # 2. 请求 userLogin 页, 获取 cookie
    # 创建 OpenerDirector 实例
    cookie = http.cookiejar.LWPCookieJar("cookie12306")
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)

    # 从文件加载 cookie
    cookie.load(ignore_discard=True)

    # 构造 Request
    user_login_postdata = {
        "_json_att": ""
    }
    user_login_postdata = urllib.parse.urlencode(user_login_postdata).encode("utf-8")
    req = urllib.request.Request(user_login_url, user_login_postdata, user_login_headers)

    # 请求 userLogin
    user_login_response = opener.open(req, timeout=5)

    # 存储 cookie 到文件
    cookie.save(ignore_discard=True, ignore_expires=True)

    # 关闭请求
    user_login_response.close()

    # 3. 请求 umatk 页, 获取 tk
    # 创建 OpenerDirector 实例
    cookie = http.cookiejar.LWPCookieJar("cookie12306")
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)

    # 从文件加载 cookie
    cookie.load(ignore_discard=True)

    # 构造 Request
    uamtk_postdata = {
        "appid": "otn"
    }
    uamtk_postdata = urllib.parse.urlencode(uamtk_postdata).encode("utf-8")
    req = urllib.request.Request(uamtk_url, uamtk_postdata, uamtk_headers)

    # 请求 uamtk
    uamtk_response = opener.open(req, timeout=5)

    # 获取并解析 Response
    uamtk_response_xml = uamtk_response.read().decode("utf-8")
    new_app_tk = re.findall("<newapptk>([a-zA-Z0-9\-\_]+)</newapptk>", uamtk_response_xml)[0]
    #print(new_app_tk)

    # 关闭请求
    uamtk_response.close()

    # 4. 请求 uamauthclient 页, 获取 cookie
    # 创建 OpenerDirector 实例
    cookie = http.cookiejar.LWPCookieJar("cookie12306")
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)

    # 从文件加载 cookie
    cookie.load(ignore_discard=True)

    # 构造 Request
    uamauthclient_postdata = {
        "tk": new_app_tk
    }
    uamauthclient_postdata = urllib.parse.urlencode(uamauthclient_postdata).encode("utf-8")
    req = urllib.request.Request(uamauthclient_url, uamauthclient_postdata, uamauthclient_headers)

    # 请求 uamtk
    uamauthclient_response = opener.open(req, timeout=5)

    # 存储 cookie 到文件
    cookie.save(ignore_discard=True, ignore_expires=True)

    # 关闭请求
    uamauthclient_response.close()


# 验证码处理
def validate_captcha():
    # 1. 从服务器获取验证码图片
    # 创建 OpenerDirector 实例
    cookie = http.cookiejar.LWPCookieJar("cookie12306")
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    
    # 构造 Request
    req = urllib.request.Request(get_captcha_url, headers=get_captcha_headers)
    
    # 关闭 SSL 验证
    ssl._create_default_https_context = ssl._create_unverified_context
    
    # 发送获取验证码请求
    captcha_response = opener.open(req, timeout=5)

    # 存储 cookie 到文件
    cookie.save(ignore_discard=True, ignore_expires=True)

    # 存储验证码图片
    with open('captcha12306.jpg', 'wb') as f:
        f.write(captcha_response.read())

    # 关闭请求
    captcha_response.close()

    # 2. 输入验证码并处理
    # 输入验证码
    print("验证码图片已保存在当前目录下, 请手动打开验证码图片")
    raw_captcha_value = input("第一行图片序号从左至右为1-4, 第二行图片序号从左至右为5-8\n请输入所有符合的图片序号并用逗号隔开\n> ")

    # 读取输入的验证码序号, 计算出验证码的值
    raw_captcha_value = [int(c.strip()) for c in raw_captcha_value.split(",") if c.strip()]
    l = []
    for cv in raw_captcha_value:
        cvx = cv
        if cvx > 4:
            cvx = cvx - 4
        random.seed(datetime.datetime.now())
        x = (cvx - 1) * 75 + random.randrange(1, 74)
        y = (cv // 5) * 75 + random.randrange(1, 74) 
        l.append(str(x))
        l.append(str(y))
    captcha_value = ",".join(l)

    # 3. 检查输入的验证码是否正确
    # 创建 OpenerDirector 实例
    cookie = http.cookiejar.LWPCookieJar("cookie12306")
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)

    # 从文件加载 cookie
    cookie.load(ignore_discard=True)

    # 构造 Request
    check_captcha_postdata = {
        "answer": captcha_value,
        "login_site": "E",
        "rand": "sjrand"
    }
    check_captcha_postdata = urllib.parse.urlencode(check_captcha_postdata).encode("utf-8")
    req = urllib.request.Request(check_captcha_url, data=check_captcha_postdata, headers=check_captcha_headers)

    # 发送检查验证码请求
    check_captcha_response = opener.open(req, timeout=5)
    
    # 存储 cookie 到文件
    cookie.save(ignore_discard=True, ignore_expires=True)

    # 获取并解析 Response, 打印验证信息
    if check_captcha_response.info()["Content-Encoding"] == "gzip":
        buf = io.BytesIO(check_captcha_response.read())
        f = gzip.GzipFile(fileobj=buf)
        check_captcha_response_json = f.read().decode("utf-8")
        check_captcha_response_dict = json.loads(check_captcha_response_json)
        print(check_captcha_response_dict.get("result_message"))

    # 关闭请求
    check_captcha_response.close()
    return check_captcha_response_dict.get("result_code")


if __name__ == "__main__":
    if is_login():
        print("您已经登录了!!")
        sys.exit(0)
    else:
        while True:
            result_code = validate_captcha()
            if result_code == "4":
                break
        username = input("请输入你的用户名: ")
        password = input("请输入你的密码: ")
        login(username, password)


