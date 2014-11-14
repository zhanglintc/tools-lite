#!/usr/bin/python
#-*- coding: utf-8 -*-

import os, sys, urllib
import datetime, time
import subprocess
import platform

reload(sys)
sys.setdefaultencoding('utf8')

today = str(datetime.date.today()) # something like: 2014-11-10
cur_time = (datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')) # 2014-11-10 15:12:40

web_cotent = urllib.urlopen("https://github.com/zhanglintc") # open website

line = True
count = None
fw = open(today+'.log', 'w')
while line:
    line = web_cotent.readline()

    # write web_content to log file
    fw.write(line)

    # if get web_content error, exit with code 100, so caller.py will recall this script
    if 'wrong' in line:
        sys.exit(100)

    if line and count == None: # readline isn't None means urlopen success, initialize count as 0
        count = 0

    if today in line: # find today
        idx = line.find('data-count')
        count = line[idx + 12 : idx + 13] # 12 & 13 to find count of today's commits
        break

fw.close()

send_content = "Until {}, {} commits has pushed.  #GitHub reminder#".format(cur_time, count)
# send_command = 'wb -t "{}"'.format(send_content) # for weibo
send_command = 'echo "{}" | mutt -s "GitHub Report" zhanglintc623@gmail.com'.format(send_content) # for mail

if count != None: # if count is initialized, send weibo
    if 'Linux' in platform.platform():
        sp = subprocess.Popen(["/bin/bash", "-i", "-c", send_command])
        sp.communicate()
    else:
        os.system(send_command)

    print(send_command)

else: # else exit as 100
    sys.exit(100)

try:
    raw_input()
except:
    pass


