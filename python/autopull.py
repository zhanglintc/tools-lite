#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import json
import os

# repos = [
#     #### zhanglintc ####
#     'git@github.com:zhanglintc/tools-lite.git',
#     'git@github.com:zhanglintc/leetcode.git',
#     'git@github.com:zhanglintc/wb.git',
#     'git@github.com:zhanglintc/snake.git',
#     'git@github.com:zhanglintc/SourcePrac.git',
#     'git@github.com:zhanglintc/zhanglintc.github.io.git',
#     'git@github.com:zhanglintc/5th.git',
#     'git@github.com:zhanglintc/sanguosha.git',
#     'git@github.com:zhanglintc/daDoudou.git',
#     'git@github.com:zhanglintc/SetWallpaper.git',

#     #### Theodolite ####
#     'git@github.com:Theodolite/3plus2.git',
# ]

# /home/lane
base_path = os.path.expanduser('~')

def gitbak(userName):
    repos = []
    recv = urllib2.urlopen("https://api.github.com/users/{0}/repos".format(userName))
    raw = recv.read()
    dikt = json.loads(raw)
    for item in dikt:
        repos.append(item["ssh_url"])

    if not os.path.exists('{0}/gitbak/{1}'.format(base_path, userName)):
        os.makedirs('{0}/gitbak/{1}'.format(base_path, userName))

    dirs = os.listdir('{0}/gitbak/{1}'.format(base_path, userName))

    for repo in repos:
        repoName = repo.split('/')[1][:-4]
        if repoName not in dirs:
            os.system('cd {0}/gitbak/{1} && git clone {2}'.format(base_path, userName, repo))

        else:
            os.system('cd {0}/gitbak/{1}/{2} && git pull'.format(base_path, userName, repoName))

if __name__ == '__main__':
    gitbak("zhanglintc")
    gitbak("Theodolite")

os.system('date >> {0}/gitbak/gitbak.log'.format(base_path))


