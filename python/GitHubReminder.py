# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, urllib
import datetime

reload(sys)
sys.setdefaultencoding('utf8')

today = str(datetime.date.today()) # something like: 2014-11-10

web_cotent = urllib.urlopen("https://github.com/zhanglintc") # open website

line = True
while line:
    line = web_cotent.readline()
    if today in line: # find today
        idx = line.find('data-count')
        content = line[idx : idx + 14]
        break

# wb -t "data-count="1"  #GitHub reminder#"
os.system('wb -t "{}"'.format(content + '  #GitHub reminder#'))

try:
    raw_input()
except:
    pass


