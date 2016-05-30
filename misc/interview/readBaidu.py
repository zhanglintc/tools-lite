#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib, urllib2
import time, re

def readBaidu(url, pages):
    html = urllib.urlopen(url).read()

    soup = BeautifulSoup(html, "html.parser")

    items = []
    for item in soup.body.select('div[class=result]'):
        dikt = {}

        title = item.h3.a.text
        time_elapsed = int(re.search(".*(\d).*", item.p.text).group(1))
        publisher = re.search("(.*?)\d.*", item.p.text).group(1)
        publish_time = time.strftime ("%Y-%m-%d %X", time.localtime(time.time() - time_elapsed * 60 * 24) )
        abstract = re.search( "/p>(.*)<span", str(item.find("div")) ).group(1).replace("<em>", "").replace("</em>", "")

        dikt["title"] = title
        dikt["publisher"] = publisher
        dikt["time"] = publish_time
        dikt["abstract"] = abstract

        items.append(dict(dikt))

    pages.append(items[:])
    next_page = "http://www.baidu.com" + soup.body.find("a", text="下一页>").attrs["href"]
    return next_page

if __name__ == '__main__':
    target = "http://news.baidu.com/ns?word=%B0%A2%C0%EF%B0%CD%B0%CD&tn=news&from=news&cl=2&rn=20&ct=1"
    pages = []

    for i in range(2):
        target = readBaidu(target, pages)

    print pages


