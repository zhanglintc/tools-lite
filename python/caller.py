# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys

command = r"python {}\GitHubReminder.py".format(sys.path[0])

# if os.system() exit with not code 0, recall it
while os.system(command):
    print('failed, try again\n')

