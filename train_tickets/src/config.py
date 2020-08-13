# -*- coding: utf-8 -*-
# Aug 01 2017
# by Sin


"""
configuration
"""

import random


# 站点编码的地址
station_code_url = (
    "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?"
    "station_version=1.9020"
)


# 请求站点编码地址的头部信息
station_code_headers = {
    "Host": "kyfw.12306.cn",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,en-US;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}


# 查询火车票的地址模板
ticket_query_url_template = (
    "https://kyfw.12306.cn/otn/leftTicket/query?"
    "leftTicketDTO.train_date={}&"
    "leftTicketDTO.from_station={}&"
    "leftTicketDTO.to_station={}&"
    "purpose_codes=ADULT"
)


# 请求查询火车票地址的头部信息
ticket_query_headers = {
    "Host": "kyfw.12306.cn",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Accept": "*/*",
    "Accept-Language": "zh-CN,en-US;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "If-Modified-Since": "0",
    "Cache-Control": "no-cache",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://kyfw.12306.cn/otn/leftTicket/init",
    "Connection": "keep-alive"
}


# 获取验证码地址
get_captcha_url = (
    "https://kyfw.12306.cn/passport/captcha/captcha-image?"
    "login_site=E&"
    "module=login&"
    "rand=sjrand&"
    "%.16f"
) % random.random()


# 请求获取验证码地址的头部信息
get_captcha_headers = {
    "Host": "kyfw.12306.cn",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Accept": "*/*",
    "Accept-Language": "zh-CN,en-US;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://kyfw.12306.cn/otn/login/init",
    "Connection": "keep-alive"
}


# 检查验证码地址
check_captcha_url = "https://kyfw.12306.cn/passport/captcha/captcha-check"


# 请求检查验证码地址的头部信息
check_captcha_headers = {
    "Host": "kyfw.12306.cn",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0", 
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,en-US;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "x-requested-with": "XMLHttpRequest",
    "Referer": "https://kyfw.12306.cn/otn/login/init",
    "Connection": "keep-alive"
}


# 登录地址
login_url = "https://kyfw.12306.cn/passport/web/login"


# 请求登录地址的头部信息
login_headers = {
    "Host": "kyfw.12306.cn",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0", 
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,en-US;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "x-requested-with": "XMLHttpRequest",
    "Referer": "https://kyfw.12306.cn/otn/login/init",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}


# userlogin 地址
user_login_url = "https://kyfw.12306.cn/otn/login/userLogin"


# 请求 userlogin 地址的头部信息
user_login_headers = {
    "Host": "kyfw.12306.cn",
    "Origin": "https://kyfw.12306.cn",
    "Referer": "https://kyfw.12306.cn/otn/login/init",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0", 
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,en-US;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}


# uamtk url
uamtk_url = "https://kyfw.12306.cn/passport/web/auth/uamtk"


# 请求 uamtk 地址的头部信息
uamtk_headers = {
    "Host": "kyfw.12306.cn",
    "Origin": "https://kyfw.12306.cn",
    "Referer": "https://kyfw.12306.cn/otn/passport?redirect=/otn/login/userLogin",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0", 
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,en-US;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "X-Requested-With": "XMLHttpRequest"
}

# uamauthclient url
uamauthclient_url = "https://kyfw.12306.cn/otn/uamauthclient"


# 请求 uamauthclient 地址的头部信息
uamauthclient_headers = {
    "Host": "kyfw.12306.cn",
    "Origin": "https://kyfw.12306.cn",
    "Referer": "https://kyfw.12306.cn/otn/passport?redirect=/otn/login/userLogin",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0", 
    "Accept": "*/*",
    "Accept-Language": "zh-CN,en-US;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "X-Requested-With": "XMLHttpRequest"
}


# 个人中心地址
profile_url = "https://kyfw.12306.cn/otn/modifyUser/initQueryUserInfo"


# 请求个人中心地址的头部信息
profile_headers = {
    "Host": "kyfw.12306.cn",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0", 
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,en-US;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}



