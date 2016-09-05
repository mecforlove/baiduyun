#!/usr/bin/python  
# -*- coding:utf-8 -*-  
# File Name: upload.py
# Author: meczhang
# Mail: mecforlove@outlook.com
# Created Time: 2016-08-24 14:25:36

import urllib2

def main():
    cookie = 'BDUSS=GxXVHFmbjYtSHlNaFZ0WUIySkFjUUdpYmx0eUFrMjZ4YUgwUXpaczE4MHduLVJYQVFBQUFBJCQAAAAAAAAAAAEAAAAy-npit6LQocqxueIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADASvVcwEr1Xb'
    url = 'http://c.pcs.baidu.com/rest/2.0/pcs/file?method=upload&path=%2ftest%2fdemo.txt&app_id=266719'
    req = urllib2.Request(url, data='file='+open(r'Baidu.txt', 'rb').read())
    req.add_header('Cookie', cookie)
    resp = urllib2.urlopen(req)
    print resp.read()

if __name__ == '__main__':
    main()
