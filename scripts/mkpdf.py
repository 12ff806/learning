#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import urllib.request
import urllib.error
import urllib.parse
from html.parser import HTMLParser
import re
import os
import pdfkit


html_template = """
<!DOCTYPE html>
<html lang="zh-CN">
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <h1 style="text-align: center">{}</h1>
        {}
    </body>
</html>
"""


def func(m):
    domain = "https://www.liaoxuefeng.com"
    if not m.group(2).startswith("https"):
        rtn = "".join([m.group(1), domain, m.group(2), m.group(3)])
        return rtn
    else:
        return "".join([m.group(1), m.group(2), m.group(3)])


class URLParser(HTMLParser):
    """
    解析所有章节的 URL
    """
    def __init__(self, base_url):
        HTMLParser.__init__(self)
        self.__base_url = base_url
        self.__flag = False
        self.__count = 0
        self.urls = []

    def handle_starttag(self, tag, attrs):
        if tag == "ul":
            for attr in attrs:
                if attr[0] == "class" and attr[1] == "uk-nav uk-nav-side":
                    self.__count = self.__count + 1
                    if self.__count == 2:
                        self.__flag = True
        elif self.__flag and tag == "a":
            for attr in attrs:
                if attr[0] == "href":
                    self.urls.append(self.__base_url + attr[1])

    def handle_endtag(self, tag):
        if self.__flag and tag == "ul":
            self.__flag = False
            self.__count = -1


def get_toc_urls(index_url):
    """
    获取所有章节的 URL
    """
    parse_index_url = urllib.parse.urlparse(index_url)
    base_url = parse_index_url.scheme + "://" + parse_index_url.netloc
    req = urllib.request.Request(index_url)
    try:
        response = urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        print(e.reason)
    else:
        url_parser = URLParser(base_url)
        url_parser.feed(response.read().decode("utf-8"))
        return url_parser.urls
    finally:
        response.close()


def get_content(url):
    """
    获取文章内容
    """
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        print(e.reason)
    else:
        response_text = response.read().decode("utf-8")
        start = response_text.find("<div class=\"x-content\"")
        if start == -1:
            return None
        title_start = response_text.find("<h4>", start)
        if title_start == -1:
            return None
        title_end = response_text.find("</h4>", title_start)
        title = response_text[title_start + 4: title_end]
        content_start = response_text.find("<div class=\"x-wiki-content x-main-content\">", title_end)
        if content_start == -1:
            return None
        content_end = response_text.find("</div>", content_start)
        content = response_text[content_start: content_end + 7]
        
        pattern = "(<img .*?src=\")(.*?)(\")"        
        content = re.compile(pattern).sub(func, content)
        html = html_template.format(title, content)
        return html
    finally:
        response.close()


if __name__ == "__main__":
    index_url = "https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"
    urls = get_toc_urls(index_url)
    htmls = []
    for index, url in enumerate(urls):
        html = get_content(url)
        file_name = ".".join([str(index), "html"])
        with open(file_name, "w") as f:
            f.write(html)
        htmls.append(file_name)

    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'outline-depth': 2
    }
    pdfkit.from_file(htmls, "python3_book_from_liao.pdf", options=options)
    for html_file in htmls:
        os.remove(html_file)


