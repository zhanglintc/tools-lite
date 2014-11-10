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
        count = line[idx + 12 : idx + 13] # 12 & 13 to find count of today's commits
        break

send_content = "Until {}, {} commits has pushed.  #GitHub reminder#".format(cur_time, count)
send_command = 'wb -t "{}"'.format(send_content)
os.system(send_command)

try:
    raw_input()
except:
    pass


