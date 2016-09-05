#!/usr/bin/python  
# -*- coding:utf-8 -*-  
# File Name: test.py
# Author: meczhang
# Mail: mecforlove@outlook.com
# Created Time: 2016-08-12 01:48:25

import utils
import urllib2
import re
import sys


def magnets(key):
	"""通过关键字搜索磁力链接
	返回磁力链接的列表
	"""
	key = urllib2.quote(key)   # URL编码转换
	url = 'http://pandilao.com/s/' + str(key)
	req = urllib2.Request(url)
	# 添加头部伪装成浏览器行为
	req.add_header('User-Agent', 
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')
	opener = utils.get_opener()
	resp = opener.open(req)
	html = resp.read()
	result = re.findall(r'(magnet:?[^\"]+).*title="(.*)"\s', html)
	return result

	

if __name__ == '__main__':
	result = magnets(sys.argv[1])
	for i in result:
		print i[1], ': ', i[0]
