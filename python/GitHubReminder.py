#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Check https://github.com/zhanglintc and get the day's commit's count,
if everything goes right, send a mail to foxmail and exit with code 0.
Otherwise exit with code 100.

Exit code:
0  : success
100: fail
"""

import os, sys, urllib
import datetime, time
import subprocess
import platform
import re

def github_reminder():
    reload(sys)
    sys.setdefaultencoding('utf8')

    today = str(datetime.date.today()) # something like: 2014-11-10
    cur_time = (datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')) # 2014-11-10 15:12:40
    file_name = (datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')) + '.log' # 20141110_151240.log

    web_cotent = urllib.urlopen("https://github.com/zhanglintc?period=daily") # open website

    line  = True
    error = True
    count = None
    pushed_detail = ""
    fw = open(file_name, 'w')
    while line:
        line = web_cotent.readline()

        # write web_content to log file
        fw.write(line)

        # if 'data-count' is found, means connect is OK, set error as False
        if error and 'data-count' in line:
            error = False

        # if get web_content error, exit with code 100, so caller.py will recall this script
        if 'wrong' in line:
            if error: # really error, this make script hasn't get data-count
                fw.close()
                os.remove(file_name)
                return 100
            else: # something occurred after get data-count, doesn't matter
                break

        if line and count == None: # readline isn't None means urlopen success, initialize count as 0
            count = 0

        if today in line: # find today
            count = line.split('\"')[11] # today's commit is in 11th position
            # break # not break here to find pushed_details

        if 'Pushed' in line:
            line = re.sub('^ *', '', line) # strip spaces in the beginning of this line
            line = re.sub('</a>', '', line) # remove </a>
            pushed_detail += line

    fw.close()

    # send_content = "Until {}, {} commits has pushed.  #GitHub reminder#".format(cur_time, count)
    send_content = "You have {} {} today\n{}\n\n{}\n#GitHub reminder#\n".format\
        (
            count,
            'commit' if count < 2 else 'commits',
            cur_time,
            pushed_detail,
        )
    # send_command = 'wb -t "{}"'.format(send_content) # for weibo
    send_command = 'echo "{}" | mutt -s "GitHub Report" zhanglintc623@foxmail.com'.format(send_content) # for mail

    if count != None: # if count is initialized, do command
        print("sending...\n")

        if 'Linux' in platform.platform():
            sp = subprocess.Popen(["/bin/bash", "-i", "-c", send_command])
            sp.communicate()
        else:
            os.system(send_command)

        print(send_command + '\n')

        return 0

    else: # else exit as 100
        return 100

if __name__ == '__main__':
    github_reminder()

    try:
        raw_input()
    except:
        pass


