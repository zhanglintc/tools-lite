#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, urllib
import datetime, time
import re

CUR_TIME = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S') # 20141110_151240
LOG_FILE = CUR_TIME + '.log' # 20141110_151240.log

TARGET_URL = "http://photo.163.com/foreverse@126/pp/slide/12703047.html#pid=38152323"

mc = re.search("http.?://(.*?)/.*", TARGET_URL + "/")
siteName = mc.group(1)
folderName = "{}_{}".format(siteName, CUR_TIME)

if not os.path.exists(folderName):
    os.system("mkdir {}".format(folderName))

web_cotent = urllib.urlopen(TARGET_URL) # open website

content = web_cotent.read()
mc = re.findall("http.//[^ ]*?jpg", content)

picNumbers = len(mc)
print("download start...\n")

idx = 1
for url in mc:
    picName = url.split("/")[-1]
    print("{} --- {}/{}".format(picName, idx, picNumbers))
    idx += 1

    file_path, headers = urllib.urlretrieve(url)
    with open(file_path, "rb") as fr:
        data = fr.read()

    with open("{}/{}".format(folderName, picName), "wb") as fw:
        fw.write(data)

print("")
print("download completed...")

try:
    input()
except:
    pass

