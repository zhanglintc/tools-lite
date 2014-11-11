# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys

command = r"python {}\GitHubReminder.py".format(sys.path[0])

while os.system(command):
    print('failed, try again\n')

