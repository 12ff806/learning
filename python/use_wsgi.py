#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from wsgiref.simple_server import make_server
# 自己写的 hello_web.py 里的 application 函数
from hello_web import application 


# 创建一个服务器, IP地址为空, 端口8000, 处理函数是 application
httpd = make_server("", 8000, application)
print("Serving HTTP on port 8000....")
# 开始监听 HTTP 请求
httpd.serve_forever()


