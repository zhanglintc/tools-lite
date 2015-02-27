#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Check https://github.com/zhanglintc and get the day's commit's count
and show it directly.
"""

import os, urllib
import datetime, time
import re
from ColorfulPrint import cprint

TODAY = str(datetime.date.today()) # something like: 2014-11-10
CUR_TIME = (datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')) # 2014-11-10 15:12:40
LOG_FILE = (datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')) + '.log' # 20141110_151240.log

def github_reminder():
    web_cotent = urllib.urlopen("https://github.com/zhanglintc?period=daily") # open website
    web_cotent = urllib.urlopen("https://github.com/zhanglintc?period=daily") # do it twice

    line  = True
    error = True
    count = None
    pushed_detail = ""
    fw = open(LOG_FILE, 'w')
    while line:
        # read each line while not the end
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
                os.remove(LOG_FILE)
                return 100
            else: # something occurred after get data-count, doesn't matter
                break

        if line and count == None: # readline isn't None means urlopen success, initialize count as 0
            count = 0

        if '"{}"'.format(TODAY) in line: # find TODAY, TODAY must surrounded with quotation marks like "2014-11-10"
            count = line.split('\"')[11] # today's commit is in 11th position

        if 'Pushed' in line:
            line = re.sub('^ *', '', line) # strip spaces in the beginning of this line
            line = re.sub('</a>', '', line) # remove </a>
            pushed_detail += line

        if "/issues/" in line and '"title"' in line:
            line = re.sub('</a>', '', line) # remove </a>
            line = line.split('>')[-1] # issue detail is in last position
            pushed_detail += ("Issues: " + line)

    fw.close()

    send_content = "You have pushed [{}, red] {} until now\n{}\n\n{}\n#GitHub reminder#\n".format\
        (
            count,
            "commit" if int(count) < 2 else "commits",
            CUR_TIME,
            pushed_detail,
        )

    # if don't want to see log file, use the code next line
    # if want to see log file, then comment the code below
    os.remove(LOG_FILE) # remove log file any way, zhanglin 2014.11.20

    return send_content

if __name__ == '__main__':
    cprint(github_reminder())

    try:
        raw_input()
    except:
        pass


