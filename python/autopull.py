#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import os

# /home/lane
base_path = os.path.expanduser('~')
gitbak_dir = f"{base_path}/gitbak/"
token_file = f"{gitbak_dir}/.token_file"

with open(token_file, 'rb') as fr:
    token_file_content = fr.read()

"""
    URL which able to retrieve PRIVATE repos:
        `https://api.github.com/search/repositories?q=user:zhanglintc`
    Note: `user` can be replaced with `org`, if you're tring to retrieve organization information.
    Refer: https://github.community/t/how-to-get-list-of-private-repositories-via-api-call/120175/2


    URL which only able to retrieve PUBLIC repos:
        `https://api.github.com/users/zhanglintc/repos`

    How to provide a access token:
        `https://developer.github.com/changes/2020-02-10-deprecating-auth-through-query-param/`
"""


token = 'token_file_content'
url = "https://api.github.com/search/repositories"


def gitbak(userName):
    params = {
        'q': f'user:{userName}',
        'per_page': 999,
    }
    headers = {
        'Authorization': f'token {token}',
    }
    res = requests.get(url, params=params, headers=headers)

    o = json.loads(res.text)
    items = o['items']
    repos = [it['ssh_url'] for it in items]

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


