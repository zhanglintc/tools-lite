# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import GitHubReminder

#command = r"python {}\GitHubReminder.py".format(sys.path[0])

# if GitHubReminder.github_reminder() returned with not code 0, recall it
while GitHubReminder.github_reminder(Auto_Commit_Flag = True):
    print('zhanglin failed, try again\n')


# below is WuHong special process...
Wuhong_Mail_List = [
    "yaodao5000@yahoo.co.jp",
    # "zhanglintc623@foxmail.com",]
Wuhong_Github_URL = "https://github.com/sheriseanes?period=daily"
while GitHubReminder.github_reminder(MailList = Wuhong_Mail_List, GITHUB_URL = Wuhong_Github_URL, Auto_Commit_Flag = False):
    print('wuhong failed, try again\n')


# below is Houliyuan special process...
Houliyuan_Mail_List = [
    "349655336@qq.com",
    "zhanglintc623@foxmail.com",]
Houliyuan_Github_URL = "https://github.com/Pang327?period=daily"
while GitHubReminder.github_reminder(MailList = Houliyuan_Mail_List, GITHUB_URL = Houliyuan_Github_URL, Auto_Commit_Flag = False):
    print('houliyuan failed, try again\n')



