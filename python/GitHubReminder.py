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

with open('.smpass', 'rb') as fr:
    PASSWORD = fr.read().strip()

MailType = 'sendemail' # 'mutt'

SENDFROM = "zhanglintc@163.com"
USERNAME = "zhanglintc@163.com"

if not PASSWORD:
    PASSWORD = "YOURPASSWORD"
else:
    pass

MailList = [
    "zhanglintc623@foxmail.com",
    "0801jcjhz@163.com",
]

TODAY = str(datetime.date.today()) # something like: 2014-11-10
CUR_TIME = (datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')) # 2014-11-10 15:12:40
LOG_FILE = (datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')) + '.log' # 20141110_151240.log

def make_commands(send_content):
    send_commands = []

    for mailto in MailList:
        if MailType == 'sendemail':
            send_commands.append(
                'sendEmail -f {0} -t {1} -s smtp.163.com -xu {2} -xp {3} -u "GitHub Report" -m "{4}"'.format(
                    SENDFROM, # 0
                    mailto,   # 1
                    USERNAME, # 2
                    PASSWORD, # 3
                    send_content, # 4
                    )
                )

        elif MailType == 'mutt':
            send_commands.append('echo "{0}" | mutt -s "GitHub Report" {1}'.format(send_content, mailto))

        else:
            pass

    return send_commands


def auto_commit():
    """
    auto push a commit to GitHub

    return send_commands: a list of commands
    """

    cd_command = "cd {} &&".format(sys.path[0])

    os.system('{} git pull'.format(cd_command))
    os.system('{} date >> auto_commit_file'.format(cd_command))
    os.system('{} git add auto_commit_file'.format(cd_command))
    os.system('{} git commit -m "{} auto commit"'.format(cd_command, CUR_TIME))
    os.system('{} git push'.format(cd_command))

    send_content = "You haven't pushed any commit today\nso we did a auto-commit for you\n\n#GitHub reminder#"
    send_commands = make_commands(send_content)

    return send_commands

def github_reminder():
    reload(sys)
    sys.setdefaultencoding('utf8')

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

        if TODAY in line: # find today
            count = line.split('\"')[11] # today's commit is in 11th position

        if 'Pushed' in line:
            line = re.sub('^ *', '', line) # strip spaces in the beginning of this line
            line = re.sub('</a>', '', line) # remove </a>
            pushed_detail += line

    fw.close()

    send_content = "You have pushed {} {} until now\n{}\n\n{}\n#GitHub reminder#\n".format\
        (
            count,
            "commit" if int(count) < 2 else "commits",
            CUR_TIME,
            pushed_detail,
        )
    send_commands = make_commands(send_content)

    ##########################################
    # if localtime is between 23:00 and 24:00 but still no commit
    # do automatically commit function

    if time.localtime().tm_hour == 23 and count == '0':
        send_commands = auto_commit()
    ##########################################

    # if don't want to see log file, use the code next line
    # if want to see log file, then comment the code below
    os.remove(LOG_FILE) # remove log file any way, zhanglin 2014.11.20

    if count != None: # if count is initialized, do command
        print("sending...\n")

        for send_command in send_commands:
            if 'Linux' in platform.platform():
                # sp = subprocess.Popen(["/bin/bash", "-i", "-c", send_command])
                # sp.communicate()
                os.system(send_command)

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


