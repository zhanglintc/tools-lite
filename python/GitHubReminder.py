# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, urllib
import datetime, time

reload(sys)
sys.setdefaultencoding('utf8')

today = str(datetime.date.today()) # something like: 2014-11-10
cur_time = (datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')) # 2014-11-10 15:12:40

web_cotent = urllib.urlopen("https://github.com/zhanglintc") # open website

line = True
while line:
    line = web_cotent.readline()
    if today in line: # find today
        idx = line.find('data-count')
        content = line[idx : idx + 14]
        break

send_content = "{}, {}  #GitHub reminder#".format(cur_time, content)
os.system('wb -t "{}"'.format(send_content))

try:
    raw_input()
except:
    pass


