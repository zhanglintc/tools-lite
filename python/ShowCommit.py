#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Check https://github.com/zhanglintc and get the day's contributions
and show it directly.
"""

import os, urllib
import datetime, time
import re
from ColorfulPrint import cprint

TODAY = str(datetime.date.today()) # something like: 2014-11-10
CUR_TIME = (datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')) # 2014-11-10 15:12:40
LOG_FILE = (datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')) + '.log' # 20141110_151240.log

def github_reminder(targetURL):
    cprint("[" + targetURL.split("/")[-1].split("?")[0] + ":, red]\n")
    web_content = urllib.urlopen(targetURL) # open website

    line  = True
    error = True
    count = None
    pushed_detail = ""
    fw = open(LOG_FILE, 'w')
    while line:
        # read each line while not the end
        line = web_content.readline()

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

        if TODAY in line and "data-count" in line:
            mc = re.search('data-count="(\d+)"', line)
            count = int(mc.group(1))

    fw.close()

    send_content = "You have made [{}, red] {} until now\n{}\n\n{}\n#GitHub reminder#\n".format\
        (
            count,
            "contribution" if int(count) < 2 else "contributions",
            CUR_TIME,
            pushed_detail,
        )

    # if don't want to see log file, use the code next line
    # if want to see log file, then comment the code below
    os.remove(LOG_FILE) # remove log file any way, zhanglin 2014.11.20

    return send_content

if __name__ == '__main__':
    cprint(github_reminder("https://github.com/zhanglintc?tab=overview&from={0}".format(TODAY)) + "\n")
    cprint(github_reminder("https://github.com/pang327?tab=overview&from={0}".format(TODAY)) + "\n")

    try:
        raw_input()
    except:
        pass


