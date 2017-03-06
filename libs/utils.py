#!/usr/bin/python  
# -*- coding:utf-8 -*-  
# File Name: utils.py
# Author: meczhang
# Mail: mecforlove@outlook.com
# Created Time: 2016-08-13 21:25:19

import urllib2


def get_opener():
    """获取要使用的opener"""
    # 设置代理
    proxy = {'http': 'proxy.tencent.com:8080'}
    proxy_support = urllib2.ProxyHandler(proxy)
    opener = urllib2.build_opener(proxy_support)
    # retunr urllib2.build_opener()
    return urllib2.build_opener()
