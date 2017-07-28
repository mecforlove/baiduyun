#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
import threading

from requests import get, head

from config import *

HEADERS = {
    'Cookie': COOKIE,
    'User-Agent': UA
}


def support_range(url, payload):
    """判断URL是否支持Range字段

    """
    resp = head(url=url, params=payload, headers=HEADERS)
    if resp.status_code == 200:
        return True
    return False


def range_download(start, end):
    pass


if __name__ == '__main__':
    url = 'http://pcs.baidu.com/rest/2.0/pcs/file'
    payload = {
        'app_id': 266719,
        'method': 'download',
        'path': '/音乐/不要爱我_莫文蔚.mp3'
    }
    print support_range(url, payload)
