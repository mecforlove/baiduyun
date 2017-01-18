#!/usr/bin/python  
# -*- coding:utf-8 -*-  
# File Name: yunapi.py
# Author: meczhang
# Mail: mecforlove@outlook.com
# Created Time: 2016-08-15 10:05:08

import urllib2
import sys
import urllib
import json
import re
import readline
from libs.pcs import YunDisk
from libs import source
from libs import utils

def phelp():
    print """
    Welcome to Yunhelper!  This is the help utility.
    quit----------------------退出程序
    cd [文件夹名称]-----------类似于cd和ls合起来的功能
    pwd-----------------------打印当前目录
    dl [文件名]---------------下载文件至本地
    dld [文件夹名]------------递归下载文件至本地
    ?-------------------------打印此帮助信息
    """

def main():
    # 测试,这里需要输入百度的一个cookie值BDUSS
    cookie = 'BDUSS=*************'  # 添加BDUSS

    curr_dir = r'/'                  # 从根目录开始
    disk = YunDisk(cookie)           # 用自己的cookie初始化百度盘
    print 'Yunhelper 1.0\nType "?" for help,type "quit" to quit.\n\n'
    disk.print_items(curr_dir)
    while True:
        cmd = raw_input('[@'+curr_dir+']>>')        # 终端提示符
        cmd = cmd.strip()            # 去掉两端空格
        if '' == cmd:
            continue
        if 'quit' == cmd:            # 键入"quit"退出程序
            print 'bye'
            break
        cmd = re.split(r'\s+', cmd)  # 分离命令生成列表

        if 'cd' == cmd[0]:
            temp = curr_dir
            if cmd[1] == r'..':      # 返回上一级目录
                try:
                    curr_dir = curr_dir[:-1]
                    curr_dir = curr_dir[:curr_dir.rfind(r'/')+1]
                    disk.print_items(curr_dir)
                except:
                    curr_dir = temp
                    print 'No such file or directory'
            else:                    # 进入特定目录
                try:
                    curr_dir = curr_dir + cmd[1] + '/'
                    disk.print_items(curr_dir)
                except:
                    curr_dir = temp
                    print 'No such file or directory'

        elif 'pwd' == cmd[0]:
            print curr_dir
        elif 'dl' == cmd[0]:
            disk.dl_file(curr_dir+cmd[1])
        elif 'dld' == cmd[0]:
            disk.dl_dir_r(curr_dir+cmd[1])
        elif '?' == cmd[0]:
            phelp()
        else:
            print 'command not found'


if __name__ == '__main__':
    main()


