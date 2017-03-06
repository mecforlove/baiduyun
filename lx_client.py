#!/usr/bin/python  
# -*- coding:utf-8 -*-  
# File Name: lx_client.py
# Author: meczhang
# Mail: mecforlove@outlook.com
# Created Time: 2016-08-19 13:15:22

import sys
from libs.source import magnets
from libs.pcs import YunDisk

if __name__ == '__main__':
    disk = YunDisk('BDUSS=************')  # 添加BDUSS
    result = magnets(sys.argv[1])
    lst = disk.lx_list()
    disk.del_lxs(lst)  # 删除离线列表中未完成的任务
    for i in result:
        disk.lx_dload(i[0], '/我的资源/' + sys.argv[1])
