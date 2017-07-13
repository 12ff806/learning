#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os


# rename file function
# remove digit from filename
def rename_files():
    file_list = os.listdir(r"/home/sins/Downloads/prank")

    saved_dir = os.getcwd()
    os.chdir("/home/sins/Downloads/prank")

    for file_name in file_list:
        saved_file_name = file_name
        i = 0
        while(i < len(file_name)):
            if file_name[i].isdigit():
                file_name = file_name[:i] + file_name[i+1:]
            else:
                i = i + 1
        os.rename(saved_file_name, file_name)
        print("Old name: " + saved_file_name + " New name: " + file_name)

    os.chdir(saved_dir)


rename_files()
