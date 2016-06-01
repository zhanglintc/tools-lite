#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib, urllib2
import time, re

class JsonDict(dict):
    """
    Copied from weibo official SDK:
    https://github.com/michaelliao/sinaweibopy

    Make a dict access more convenient,
    now you can get value from dict just like property.
    """

    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            raise AttributeError(r"'JsonDict' object has no attribute '%s'" % attr)

    def __setattr__(self, attr, value):
        self[attr] = value

def readBaidu(url, pages):
    html = urllib.urlopen(url).read()

    soup = BeautifulSoup(html, "html.parser")

    items = []
    for item in soup.body.select('div[class=result]'):
        dikt = {}

        title = item.h3.a.text
        link = item.h3.a.attrs["href"]
        time_elapsed = int(re.search(".*(\d).*", item.p.text).group(1))
        publisher = re.search("(.*?)\d.*", item.p.text).group(1).replace(u"\xa0", "")
        publish_time = time.strftime ("%Y-%m-%d %X", time.localtime(time.time() - time_elapsed * 60 * 24) )
        abstract = re.search( "/p>(.*)<span", str(item.find("div")) ).group(1).replace("<em>", "").replace("</em>", "")

        dikt["title"] = title
        dikt["link"] = link
        dikt["publisher"] = publisher
        dikt["time"] = publish_time
        dikt["abstract"] = abstract

        items.append(JsonDict(dikt))

    pages.append(items[:])
    next_page = "http://www.baidu.com" + soup.body.find("a", text="下一页>").attrs["href"]
    return next_page

if __name__ == '__main__':
    target = "http://news.baidu.com/ns?word=%B0%A2%C0%EF%B0%CD%B0%CD&tn=news&from=news&cl=2&rn=20&ct=1"
    pages = []

    for i in range(2):
        target = readBaidu(target, pages)

    page_cnt = 0
    for page in pages:
        page_cnt += 1
        item_cnt = 0
        for item in page:
            item_cnt += 1
            print "> page      =>   " + str(page_cnt)
            print "> item      =>   " + str(item_cnt)
            print "> title     =>   " + item.title
            print "> link      =>   " + item.link
            print "> publisher =>   " + item.publisher
            print "> time      =>   " + item.time
            print "> abstract  =>   " + item.abstract
            print "=============================="


