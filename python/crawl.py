#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_page(url):
    try:
        import urllib.request
        page = urllib.request.urlopen(url)
        page_content = page.read().decode("utf-8", "ignore")
        page.close()
        #print(page_content)
        return page_content
    except:
        return ""


def get_next_target(page_content):
    start_link = page_content.find("<a href=")
    if start_link == "-1":
        return None, 0
    start_quote = page_content.find("\"", start_link)
    end_quote = page_content.find("\"", start_quote + 1)
    url = page_content[start_quote + 1: end_quote]
    return url, end_quote


def get_all_links(page_content):
    while True:
        url, endpos = get_next_target(page_content)
        if url:
            print(url)
            page_content = page_content[endpos:]
        else:
            break


get_all_links(get_page("https://xkcd.com/"))
