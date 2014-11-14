# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import subprocess

command = r"python {}\GitHubReminder.py".format(sys.path[0])

# if os.system() exit with not code 0, recall it
sp = subprocess.Popen(["/bin/bash", "-i", "-c", command])
while sp.communicate():
    print('failed, try again\n')

