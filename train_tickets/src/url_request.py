#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = "Sin"

""" get page source """


import urllib.request, urllib.parse
import io, gzip
import ssl



def get_page_source(url, headers, params=None):
    """
    func params:
        url         页面url
        headers     请求头部
        params      POST请求的参数
    """

    try:
        req = urllib.request.Request(url)

        # 添加头部信息
        for h in headers:
            req.add_header(h, headers[h])

        # 处理 HTTPS 认证
        if url.split(":")[0] == "https":
            # 方法一: 使用SSL创建未经验证的上下文, 在 urlopen 中传入上下文参数
            context = ssl._create_unverified_context()

            # 方法二: 全局取消证书验证, 不用给 urlopen 传入 context 参数
            #ssl._create_default_https_context = ssl._create_unverified_context
        else:
            context = None

        # 处理 params, 并发送请求
        if not params:
            response = urllib.request.urlopen(req, context=context, timeout=10)
        else:
            data = urllib.parse.urlencode(params).encode("utf-8")
            response = urllib.request.urlopen(req, data, context=context, timeout=10)

        # 对响应的 gzip 数据解压缩
        if response.info()["Content-Encoding"] == "gzip":
            buf = io.BytesIO(response.read())
            f = gzip.GzipFile(fileobj=buf)
            page_source = f.read().decode("utf-8")
        else:
            page_source = response.read().decode("utf-8")

        response.close()
        
        return page_source
    except Exception as e:
        raise e



