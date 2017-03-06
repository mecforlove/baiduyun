#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author: meczhang

import sys
from libs.pcs import YunDisk

if len(sys.argv) == 1:
    print 'filepath is needed!'
    sys.exit(-1)

filepath = ' '.join(sys.argv[1:])
cookie = 'BDUSS=xxxxx'
disk = YunDisk(cookie)

print '**********download started**********'

if filepath.endswith('/'):
    disk.dl_dir_r(filepath)
else:
    disk.dl_file(filepath)

print '**********download ended************'
