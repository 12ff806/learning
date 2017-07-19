#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
检测B站某UP主是否更新了通灵之战的视频
如果更新了 就给我发个短信提醒我观看
"""

__author__ = "Sin"


# 取得链接url的页面内容
def get_page(url):
    try:
        import urllib.request, urllib.parse
        
        req = urllib.request.Request(url)

        # 设置请求头部信息
        req.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
        req.add_header("Accept-Language", "zh-CN,en-US;q=0.7,en;q=0.3")
        req.add_header("Connection", "keep-alive")
        req.add_header("Host", "space.bilibili.com")
        req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0")
        #req.add_header("Accept-Encoding", "gzip, deflate, br")
        #req.add_header("Cookie", "buvid3=84536F84-BB5F-4607-8499-2692679E80C439911infoc; fts=1491528720; pgv_pvi=8067768320; sid=9oej71bm; UM_distinctid=15b50fd71e59-05b194ea592374-38694646-3e8000-15b50fd71e617c; rpdid=olmpwoomqqdoplomokwpw; CNZZDATA2724999=cnzz_eid%3D1130098725-1498606334-http%253A%252F%252Fwww.bilibili.com%252F%26ntime%3D1499297535; finger=0503d1c5; biliMzIsnew=1; biliMzTs=0; DedeUserID=1482339; DedeUserID__ckMd5=0a3f286b859e06ac; SESSDATA=1c116837%2C1502509495%2C0e8076ac; bili_jct=f740ec0962c5340f3984d477baf6567f; _cnt_pm=0; _cnt_notify=34; _dfcaptcha=8be849bc5b3052fd9f57889e4f72aeb9")

        # 请求参数
        params = {
            "mid": "18199039",
            "page": "1",
            "pagesize": "100"
        }
        data = urllib.parse.urlencode(params).encode("utf-8")

        page = urllib.request.urlopen(req, data)
        page_content = page.read().decode('utf-8')
        page.close()

        #print(page_content)
        return page_content
    except Exception as e:
        raise e

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


def main():
    # 接口"https://space.bilibili.com/ajax/member/getSubmitVideos?mid=18199039&page=1&pagesize=100"
    # 可取到UP主(mid=18199039)上传的所有视频数据
    url = r"https://space.bilibili.com/ajax/member/getSubmitVideos"
    tlzz_file_path = "/tmp/tlzz"

    try:
        page_content = get_page(url)
    except Exception as e:
        print(e)

    count = get_count(page_content)
    aid_list = get_aid(page_content)
    if int(count) != len(aid_list):
        print("接口异常, 请检查接口所提供的数据!")
        return

    try:
        f = open(tlzz_file_path, "r")
        old_count = f.readline().strip()
        old_aid_list = f.readline().strip()
        f.close()
        if old_count == count:
            print("UP主还没有更新任何视频吖!")
        elif old_count < count:
            print("UP主终于上传新的视频了!")
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
            print("更新的视频的aid为:", new_aid)
        else:
            print("UP主可能删除了某些视频!")
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

