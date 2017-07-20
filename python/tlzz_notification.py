#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
检测B站某UP主是否更新了通灵之战的视频
如果更新了 就给我发个短信提醒我观看
"""

__author__ = "Sin"


import urllib.request, urllib.parse, urllib.response
from twilio.rest import Client
import io, gzip


# 发送短信
def send_msg(message_content):
    account_sid = "ACd156d1766833bd39d2bc107251a539a9"
    auth_token = "46a98e4a98dca32cc0786d838f9f0562"
    client = Client(account_sid, auth_token)
    message = client.api.account.messages.create(to="+8618501257774", from_="+18058709600", body=message_content)


# 取得上传的视频内容
def get_submit_videos_page(url):
    try:
        req = urllib.request.Request(url)

        # 设置请求头部信息
        req.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
        req.add_header("Accept-Language", "zh-CN,en-US;q=0.7,en;q=0.3")
        req.add_header("Connection", "keep-alive")
        req.add_header("Host", "space.bilibili.com")
        req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0")
        req.add_header("Accept-Encoding", "gzip, deflate, br")

        # 请求参数
        params = {
            "mid": "18199039",
            "page": "1",
            "pagesize": "100"
        }
        data = urllib.parse.urlencode(params).encode("utf-8")

        response = urllib.request.urlopen(req, data, timeout=10)
        if response.info()["Content-Encoding"] == "gzip":
            buf = io.BytesIO(response.read())
            f = gzip.GzipFile(fileobj=buf)
            page_content = f.read().decode("utf-8")
        else:
            page_content = response.read().decode("utf-8")
        response.close()

        #print(page_content)
        return page_content
    except Exception as e:
        raise e
    finally:
        if response:
            response.close()


# 取得上传的视频总数
def get_count(page_content):
    count_list = []
    while True:
        start_count = page_content.find("count")
        if start_count == -1:
            break
        end_count = page_content.find(",", start_count)
        count = page_content[start_count+7: end_count]
        count_list.append(count)
        page_content = page_content[end_count:]
    #print(count_list)
    return count_list[-1]


# 取得所有上传视频的aid号
def get_aid(page_content):
    aid_list = []
    while True:
        aid_start = page_content.find("aid")
        if aid_start == -1:
            break
        aid_end = page_content.find(",", aid_start)
        aid = page_content[aid_start+5: aid_end]
        aid_list.append(aid)
        page_content = page_content[aid_end:]
    return aid_list


# 取得单个视频页面内容
def get_aid_page(aid_url):
    try:
        req = urllib.request.Request(aid_url)

        # 设置请求头部信息
        req.add_header("Host", "www.bilibili.com")
        req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0")
        req.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
        req.add_header("Accept-Language", "zh-CN,en-US;q=0.7,en;q=0.3")
        req.add_header("Connection", "keep-alive")
        req.add_header("Accept-Encoding", "gzip, deflate") 

        response = urllib.request.urlopen(req, timeout=10)
        if response.info()["Content-Encoding"] == "gzip":
            buf = io.BytesIO(response.read())
            f = gzip.GzipFile(fileobj=buf)
            aid_page_content = f.read().decode("utf-8")
        else:
            aid_page_content = response.read().decode('utf-8')
        response.close()

        #print(aid_page_content)
        return aid_page_content
    except Exception as e:
        raise e
    finally:
        if response:
            response.close()


def check_video(aid_page_content):
    title_start = aid_page_content.find("<div class=\"v-title\"><h1 title=\"")
    if title_start == -1:
        return False
    title_end = aid_page_content.find("</h1></div>", title_start)
    title = aid_page_content[title_start: title_end]
    flag = title.find("通灵之战")
    if flag == -1:
        return False
    return True


def main():
    # 接口"https://space.bilibili.com/ajax/member/getSubmitVideos?mid=18199039&page=1&pagesize=100"
    # 可取到UP主(mid=18199039)上传的所有视频数据
    url = r"https://space.bilibili.com/ajax/member/getSubmitVideos"
    tlzz_file_path = "/tmp/tlzz"

    try:
        page_content = get_submit_videos_page(url)
    except Exception as e:
        raise e

    count = get_count(page_content)
    aid_list = get_aid(page_content)
    if int(count) != len(aid_list):
        print("接口异常, 请检查接口所提供的数据!")
        #send_msg("接口异常, 请检查接口所提供的数据!")
        return

    try:
        f = open(tlzz_file_path, "r")
        old_count = f.readline().strip()
        old_aid_list = f.readline().strip()
        f.close()
        if old_count == count:
            print("UP主还没有更新任何视频吖!")
            send_msg("UP主还没有更新任何视频吖!")
        elif old_count < count:
            f = open(tlzz_file_path, "w")
            f.write(count)
            f.write("\n")
            f.write(str(aid_list))
            f.close()
            new_aid = []
            for x in aid_list:
                flag = old_aid_list.find(x)
                if flag == -1:
                    new_aid.append(x)
            print("UP主终于上传新的视频了! 更新的视频的aid为:", new_aid)
            #send_msg("UP主终于上传新的视频了! 更新的视频的aid为: %s" % str(new_aid))

            tlzz_list = []
            for aid in new_aid:
                aid_url = "http://www.bilibili.com/video/av" + aid
                try:
                    #print(aid_url)
                    aid_page_content = get_aid_page(aid_url)
                    #print(aid_page_content)
                    tlzz_updated = check_video(aid_page_content)
                    if tlzz_updated:
                        tlzz_list.append(aid_url)
                except Exception as e:
                    raise e
            if not tlzz_list:
                print("UP主更新了视频,但是通灵之战还没有更新喔!")
            else:
                print("通灵之站更新啦!!! 地址为: %s " % str(tlzz_list))
                send_msg("通灵之站更新啦!!! 地址为: %s " % str(tlzz_list))
        else:
            print("UP主可能删除了某些视频!")
            #send_msg("UP主可能删除了某些视频!")
            f = open(tlzz_file_path, "w")
            f.write(count)
            f.write("\n")
            f.write(str(aid_list))
            f.close()
    except IOError as e:
        f = open(tlzz_file_path, "w")
        f.write(count)
        f.write("\n")
        f.write(str(aid_list))
        f.close()
    finally:
        if f:
            f.close()
    

if __name__ == "__main__":
    main()

