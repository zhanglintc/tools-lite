#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json
import requests

from concurrent import futures
from bs4 import BeautifulSoup


jieqi_json = """
{
    "jieqi_list": [
        {
            "jieqiid": 23,
            "name": "小寒",
            "pic": "http://m.46644.com/jieqi/static/images/jieqi/xh.png",
            "time": "2019-01-05 23:38:52"
        },
        {
            "jieqiid": 24,
            "name": "大寒",
            "pic": "http://m.46644.com/jieqi/static/images/jieqi/dh.png",
            "time": "2019-01-20 16:59:27"
        },
        {
            "jieqiid": 1,
            "name": "立春",
            "pic": "http://m.46644.com/jieqi/static/images/jieqi/lc.png",
            "time": "2019-02-04 11:14:14"
        },
        {
            "jieqiid": 2,
            "name": "雨水",
            "pic": "http://m.46644.com/jieqi/static/images/jieqi/ys.png",
            "time": "2019-02-19 07:03:51"
        },
        {
            "jieqiid": 3,
            "name": "惊蛰",
            "pic": "http://m.46644.com/jieqi/static/images/jieqi/jz.png",
            "time": "2019-03-06 05:09:39"
        },
        {
            "jieqiid": 4,
            "name": "春分",
            "pic": "http://m.46644.com/jieqi/static/images/jieqi/cf.png",
            "time": "2019-03-21 05:58:20"
        },
        {
            "jieqiid": 5,
            "name": "清明",
            "pic": "http://m.46644.com/jieqi/static/images/jieqi/qm.png",
            "time": "2019-04-05 09:51:21"
        },
        {
            "jieqiid": 6,
            "name": "谷雨",
            "pic": "http://m.46644.com/jieqi/static/images/jieqi/gy.png",
            "time": "2019-04-20 16:55:10"
        },
        {
            "jieqiid": 7,
            "name": "立夏",
            "pic": "http://m.46644.com/jieqi/static/images/jieqi/lx.png",
            "time": "2019-05-06 03:02:40"
        },
        {
            "jieqiid": 8,
            "name": "小满",
            "pic": "http://m.46644.com/jieqi/static/images/jieqi/xm.png",
            "time": "2019-05-21 15:59:01"
        },
        {
            "jieqiid": 9,
            "name": "芒种",
            "pic": "http://m.46644.com/jieqi/static/images/jieqi/mz.png",
            "time": "2019-06-06 07:06:18"
        },
        {
            "jieqiid": 10,
            "name": "夏至",
            "pic": "http://m.46644.com/jieqi/static/images/jieqi/xz.png",
            "time": "2019-06-21 23:54:09"
        },
        {
            "jieqiid": 11,
            "name": "小暑",
            "pic": "http://m.46644.com/jieqi/static/images/jieqi/xs.png",
            "time": "2019-07-07 17:20:25"
        },
        {
            "jieqiid": 12,
            "name": "大暑",
            "pic": "http://m.46644.com/jieqi/static/images/jieqi/ds.png",
            "time": "2019-07-23 10:50:16"
        },
        {
            "jieqiid": 13,
            "name": "立秋",
            "pic": "http://m.46644.com/jieqi/static/images/jieqi/lq.png",
            "time": "2019-08-08 03:12:57"
        },
        {
            "jieqiid": 14,
            "name": "处暑",
            "pic": "http://m.46644.com/jieqi/static/images/jieqi/cs.png",
            "time": "2019-08-23 18:01:53"
        },
        {
            "jieqiid": 15,
            "name": "白露",
            "pic": "http://m.46644.com/jieqi/static/images/jieqi/bl.png",
            "time": "2019-09-08 06:16:46"
        },
        {
            "jieqiid": 16,
            "name": "秋分",
            "pic": "http://m.46644.com/jieqi/static/images/jieqi/qf.png",
            "time": "2019-09-23 15:50:02"
        },
        {
            "jieqiid": 17,
            "name": "寒露",
            "pic": "http://m.46644.com/jieqi/static/images/jieqi/hl.png",
            "time": "2019-10-08 22:05:32"
        },
        {
            "jieqiid": 18,
            "name": "霜降",
            "pic": "http://m.46644.com/jieqi/static/images/jieqi/sj.png",
            "time": "2019-10-24 01:19:37"
        },
        {
            "jieqiid": 19,
            "name": "立冬",
            "pic": "http://m.46644.com/jieqi/static/images/jieqi/ld.png",
            "time": "2019-11-08 01:24:15"
        },
        {
            "jieqiid": 20,
            "name": "小雪",
            "pic": "http://m.46644.com/jieqi/static/images/jieqi/xx.png",
            "time": "2019-11-22 22:58:48"
        },
        {
            "jieqiid": 21,
            "name": "大雪",
            "pic": "http://m.46644.com/jieqi/static/images/jieqi/dx.png",
            "time": "2019-12-07 18:18:21"
        },
        {
            "jieqiid": 22,
            "name": "冬至",
            "pic": "http://m.46644.com/jieqi/static/images/jieqi/dz.png",
            "time": "2019-12-22 12:19:18"
        }
    ],
    "song": "春雨惊春清谷天，夏满芒夏暑相连。秋处露秋寒霜降，冬雪雪冬小大寒。"
}
"""

headers = {
    'User-Agent': 'curl/7.54.1',
    'Host': 'www.cpta.com.cn',
    'Accept': '*/*',
}


cpta_url = "http://www.cpta.com.cn/"
json_db = "/tmp/bulitin_json_db"

wechat_send_url = u"http://zhanglintc.work:8000/send?text={0}"


def read_one_link(link):
    res = requests.get(link, headers=headers)
    res.encoding = "UTF-8"
    html = res.text

    soup = BeautifulSoup(html, "html.parser")
    title = soup.select_one('.text_con > #p_title').text
    return "{title}: {link}".format(title=title, link=link)


def exam_monitor():
    res = requests.get(cpta_url, headers=headers)
    res.encoding = "UTF-8"
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
                bulitin_history = []

    for title in titles:
        if title not in bulitin_history:
            bulitin_history.append(title)

            text = requests.compat.quote(title)
            url = wechat_send_url.format(text)
            requests.get(url)

            print(title)

    import subprocess
    date = subprocess.check_output('date').rstrip().decode()
    bulitin_history.insert(0, date)

    with open(json_db, "w") as fw:
        fw.write(json.dumps(bulitin_history, indent=4))


def jieqi_monitor():
    import datetime
    today = str(datetime.date.today())  # something like: 2014-11-10
    jieqi_dict = json.loads(jieqi_json)
    jieqi_list = jieqi_dict['jieqi_list']
    jieqi_by_date = {e['time'].split()[0]: e['name'] for e in jieqi_list}

    jieqi_today = jieqi_by_date.get(today)
    if jieqi_today:
        text = u"{today} {jieqi}\n\n{song}".format(today=today, jieqi=jieqi_today, song=jieqi_dict['song'])
        url = wechat_send_url.format(text)
        requests.get(url)


def main():
    jieqi_monitor()
    exam_monitor()


if __name__ == '__main__':
    main()
