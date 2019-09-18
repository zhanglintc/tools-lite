#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json
import requests

from concurrent import futures
from bs4 import BeautifulSoup


cpta_url = "http://www.cpta.com.cn/"
json_db = "./bulitin_json_db"


def read_one_link(link):
    res = requests.get(link)
    res.encoding = "GB2312"
    html = res.text

    soup = BeautifulSoup(html, "html.parser")
    title = soup.select_one('.text_con > #p_title').text
    return title


def main():
    res = requests.get(cpta_url)
    res.encoding = "GB2312"
    html = res.text

    soup = BeautifulSoup(html, "html.parser")
    bulitin_li = soup.select('.list_14.clearfix > li')
    bulitin_para_links = map(lambda x: x.a.get("href"), bulitin_li)
    bulitin_para_links = map(lambda x: requests.compat.urljoin(cpta_url, x), bulitin_para_links)
    bulitin_para_links = list(bulitin_para_links)

    workers = min(len(bulitin_para_links), 20)
    with futures.ThreadPoolExecutor(workers) as executor:
        titles = executor.map(read_one_link, bulitin_para_links)

    bulitin_history = []
    if os.path.isfile(json_db):
        with open(json_db, "r") as fr:
            bulitin_history = fr.read()
            try:
                bulitin_history = json.loads(bulitin_history)
            except ValueError:
                pass

    for title in titles:
        if title not in bulitin_history:
            bulitin_history.append(title)

            text = requests.compat.quote(title)
            url = "http://zhanglintc.work:8000/send?text={0}".format(text)
            requests.get(url)

            print(title)

    with open(json_db, "w") as fw:
        fw.write(json.dumps(bulitin_history))


if __name__ == '__main__':
    main()
