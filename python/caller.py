# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import GitHubReminder

#command = r"python {}\GitHubReminder.py".format(sys.path[0])

# if GitHubReminder.github_reminder() returned with not code 0, recall it
while GitHubReminder.github_reminder():
    print('failed, try again\n')

