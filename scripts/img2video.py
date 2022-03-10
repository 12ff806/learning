#!/usr/bin/env python3


import os
import time
import random


transitions = [
    "fade",
    "wipeleft",
    "wiperight",
    "wipeup",
    "wipedown",
    "slideleft",
    "slideright",
    "slideup",
    "slidedown",
    "circlecrop",
    "rectcrop",
    "distance",
    "fadeblack",
    "fadewhite",
    "radial",
    "smoothleft",
    "smoothright",
    "smoothup",
    "smoothdown",
    "circleopen",
    "circleclose",
    "vertopen",
    "vertclose",
    "horzopen",
    "horzclose",
    "dissolve",
    "pixelize",
    "diagtl",
    "diagtr",
    "diagbl",
    "diagbr"
]


def imgs2video(img_list, transition=None, audio_file_path=None):
    """ imgs to video
    # 单张图片生成视频
    ffmpeg -framerate 0.4 -pattern_type glob -i './images/test*.jpg' -c:v libx264 -r 10 -pix_fmt yuv420p out.mp4
    # 将两个视频连接在一起
    ffmpeg -i out1.mp4 -i out2.mp4 -filter_complex "xfade=transition=radial:duration=1:offset=2,format=yuv420p" -y final.mp4
    # 往视频中加入音频
    ffmpeg -i video.mp4 -i audio.wav -map 0:v -map 1:a -c:v copy -shortest output.mp4
    """
    # 0 判断img_list是目录还是图片列表
    img_list_copy = img_list
    if isinstance(img_list_copy, str) and os.path.isdir(img_list_copy):
        img_list = [os.path.join(img_list_copy, x) for x in os.listdir(img_list_copy) if x.lower().endswith("png") or x.lower().endswith("jpg")]

    if not isinstance(img_list, list):
        return None

    # 1 判断图片大小是否一致
    pass

    # 2 单张图片生成视频
    pic_video_list = []
    i = 1
    for img in img_list:
        t = time.time()
        out_video_name = str(i) + "_" + "".join(str(t).split(".")) + ".mp4"
        cmd = "ffmpeg -framerate 0.25 -pattern_type glob -i '{}' -c:v libx264 -r 10 -pix_fmt yuv420p {} > /dev/null 2>&1".format(img, out_video_name)
        ret = os.system(cmd)
        if ret != 0:
            continue

        i += 1
        pic_video_list.append(out_video_name)

    # 3 将单个视频依次连接起来 转场特效可选
    if not pic_video_list:
        return None

    video_list = []
    start_video = pic_video_list[0]
    j = i
    for v in pic_video_list[1:]:
        t = time.time()
        out_video = str(i) + "_" + "".join(str(t).split(".")) + ".mp4";
        cmd = 'ffmpeg -i {} -i {} -filter_complex "xfade=transition={}:duration=1:offset={},format=yuv420p" -y {} > /dev/null 2>&1'.format(start_video, v, random.choice(transitions), str((i-j+1)*3), out_video)
        if transition:
            cmd = 'ffmpeg -i {} -i {} -filter_complex "xfade=transition={}:duration=1:offset={},format=yuv420p" -y {} > /dev/null 2>&1'.format(start_video, v, transition, str((i-j+1)*3), out_video)
        ret = os.system(cmd)
        if ret != 0:
            continue

        i += 1
        video_list.append(out_video)
        start_video = out_video
    
    # 4 往视频中加入音频(可选)
    if audio_file_path:
        t = time.time()
        final_video = str(i) + "_" + "".join(str(t).split(".")) + ".mp4"
        cmd = "ffmpeg -i {} -i {} -map 0:v -map 1:a -c:v copy -shortest {} > /dev/null 2>&1".format(start_video, audio_file_path, final_video)
        ret = os.system(cmd)
        if ret == 0:
            # 5 删除中间视频文件
            for v in pic_video_list:
                if os.path.exists(v):
                    os.remove(v)
            for v in video_list:
                if os.path.exists(v):
                    os.remove(v)
                
            return final_video

    # 5 删除中间文件
    for v in pic_video_list:
        if os.path.exists(v) and (v != start_video):
            os.remove(v)
    for v in video_list:
        if os.path.exists(v) and (v != start_video):
            os.remove(v)
    
    return start_video


if __name__ == "__main__":
    img_list = "images"
    #transition = "radial"
    transition = None
    audio_file_path = "audios/Sample-wav-file.wav"
    print(imgs2video(img_list, transition=transition, audio_file_path=audio_file_path))

