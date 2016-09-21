#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import json
import os

repos = [
    #### zhanglintc ####
    'git@github.com:zhanglintc/tools-lite.git',
    'git@github.com:zhanglintc/leetcode.git',
    'git@github.com:zhanglintc/wb.git',
    'git@github.com:zhanglintc/snake.git',
    'git@github.com:zhanglintc/SourcePrac.git',
    'git@github.com:zhanglintc/zhanglintc.github.io.git',
    'git@github.com:zhanglintc/5th.git',
    'git@github.com:zhanglintc/sanguosha.git',
    'git@github.com:zhanglintc/daDoudou.git',
    'git@github.com:zhanglintc/SetWallpaper.git',

    #### Theodolite ####
    'git@github.com:Theodolite/3plus2.git',
]

repos = []
recv = urllib2.urlopen("https://api.github.com/users/zhanglintc/repos")
raw = recv.read()
dikt = json.loads(raw)
for item in dikt:
    repos.append(item["ssh_url"])

# /home/lane
base_path  = os.path.expanduser('~')
dirs = os.listdir('{}/gitbak'.format(base_path))

for repo in repos:
    repoName = repo.split('/')[1][:-4]
    if repoName not in dirs:
        os.system('cd {}/gitbak && git clone {}'.format(base_path, repo))

    else:
        os.system('cd {}/gitbak/{} && git pull'.format(base_path, repoName))

os.system('date >> {}/gitbak/gitbak.log'.format(base_path))
# os.system('rm {}/sent'.format(base_path))


