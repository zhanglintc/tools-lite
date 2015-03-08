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
    "zhanglintc623@foxmail.com",
]

Wuhong_Github_URL = "https://github.com/sheriseanes?period=daily"

while GitHubReminder.github_reminder(MailList = Wuhong_Mail_List, GITHUB_URL = Wuhong_Github_URL, Auto_Commit_Flag = False):
    print('wuhong failed, try again\n')

