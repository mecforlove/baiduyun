#!/usr/bin/python
#  -*- coding:utf-8 -*-
# File Name: baidu.py
# Author: meczhang
# Mail: mecforlove@outlook.com
# Created Time: 2016-08-17 17:52:38
import os
import urllib2
import urllib
import utils
import json


class YunDisk(object):

    def __init__(self, cookie):
        self.cookie = cookie
        self.opener = utils.get_opener()

    def list_items(self, path):
        """
        返回path目录下的文件
        :param path: 绝对路径
        :return: 列表信息
        """
        if isinstance(path, unicode):
            path = path.encode('utf-8')
        url = 'http://pcs.baidu.com/rest/2.0/pcs/file?path=' + urllib.quote(
            path) + '&method=list&app_id=266719&by=name&order=asc&limit=0-100'
        req = urllib2.Request(url)
        req.add_header('Cookie', self.cookie)
        resp = self.opener.open(req)
        result = json.loads(resp.read())
        return result['list']

    def print_items(self, path):
        """
        打印当前目录下文件列表
        """
        lst = self.list_items(path)
        for i in lst:
            print i['server_filename']


    def dl_file(self, path):
        """
        下载指定路径下的单个文件
        :param path: 文件的绝对路径
        :return:
        """
        local_dir, filename = os.path.split(path)
        local_dir = '.' + local_dir
        # 递归创建本地目录
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)

        if isinstance(path, unicode):
            path = path.encode('utf-8')
        url = 'http://pcs.baidu.com/rest/2.0/pcs/file?path=' + urllib.quote(path) + '&method=download&app_id=266719'
        req = urllib2.Request(url)
        req.add_header('Cookie', self.cookie)
        resp = self.opener.open(req)
        # 写入文件
        with open(local_dir+'/'+filename, 'w', -1) as f:
	    while True:
                block = resp.read(20*1024)
		if not block:
		    break
                f.write(block)
        print path + '--------------------downloaded successfully'


    def dl_dir_r(self, dirpath):
        """
        递归下载文件夹dirpath下的所有文件，并将文件的目录结构保持一致
        """
        lists = self.list_items(dirpath)
        for i in lists:
            if i['isdir'] == 1:
                self.dl_dir_r(i['path'])
            else:
                self.dl_file(i['path'])


    def lx_dload(self, link, save_path):
        """
        离线下载link链接下的文件到save_path目录下
        """
        url = 'http://pcs.baidu.com/rest/2.0/pcs/services/cloud_dl?method=add_task&app_id=250528&'
        req = urllib2.Request(url)
        req.add_header('Cookie', self.cookie)
        req_data = {'save_path': save_path, 'source_url': link}
        # 放到try块里防止百度屏蔽导致错误
        try:
            resp = self.opener.open(req, urllib.urlencode(req_data))
            print resp.read()
        except:
            pass


    def lx_list(self, status=1, limit=10):
        """
        获取离线任务列表
        :param status: 离线下载状态,1代表正则下载,0代表已成功
        :param limit: 返回的任务个数
        :return: 任务列表
        """
        url = 'http://pcs.baidu.com/rest/2.0/pcs/services/cloud_dl?method=list_task&app_id=250528&'
        req = urllib2.Request(url)
        req.add_header('Cookie', self.cookie)
        req_data = {'status': 1}   
        resp = self.opener.open(req, urllib.urlencode(req_data))
        return json.loads(resp.read())


    def del_lxs(self, lst):
        """
        批量删除离线任务列表
        :param lst: 接收lx_list返回值格式
        """
        url = 'http://pcs.baidu.com/rest/2.0/pcs/services/cloud_dl?method=cancel_task&app_id=250528&'
        req = urllib2.Request(url)
        req.add_header('Cookie', self.cookie)
        for task in lst['task_info']:
            req_data = {'task_id': task['task_id']}   
            resp = self.opener.open(req, urllib.urlencode(req_data))
            if resp.read():
                print 'task: ' + str(task['task_id']) + '------deleted!'


    def __str__(self):
        return 'YunDisk: ' + self.cookie


def test():
    disk = YunDisk('ddddd')
    print disk.lx_list()


if __name__ == '__main__':
    test()
