#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, urllib
import datetime, time
import re

# global constants
TARGET_URL = "http://stackoverflow.com/"

CUR_TIME = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S') # 20141110_151240
LOG_FILE = CUR_TIME + '.log' # 20141110_151240.log

# global variables
siteName = re.search("http.?://(.*?)/.*", TARGET_URL + "/").group(1) # photo.163.com
siteTitle = re.search("<title>(.*)</title>", urllib.urlopen(TARGET_URL).read()).group(1) # Stack Overflow
folderName = "{}_{}".format(siteName, CUR_TIME) # photo.163.com_20141110_151240

def initial():
    class AppURLopener(urllib.FancyURLopener):
        version = "Mozilla/5.0"
    urllib._urlopener = AppURLopener()

    if not os.path.exists(folderName):
        os.system('mkdir "{}"'.format(folderName))

def downPic():
    print("download start...\n")

    web_cotent = urllib.urlopen(TARGET_URL) # open website
    content = web_cotent.read()
    mc = re.findall('src="(.*?jpg)"', content) # old pattern: http.//[^ ]*?jpg

    nextURL = True
    while nextURL:
        picNumbers = len(mc)
        idx = 1
        for url in mc:
            if "http" not in url:
                url = "http://" + siteName + url

            picName = url.split("/")[-1]
            print("{} --- {}/{}".format(picName, idx, picNumbers))
            idx += 1

            file_path, headers = urllib.urlretrieve(url)
            with open(file_path, "rb") as fr:
                data = fr.read()

            with open("{}/{}".format(folderName, picName), "wb") as fw:
                fw.write(data)

        try:
            nextURL = re.search('<a class="next" href="(.*?)">', content).group(1)
            if "http" not in nextURL:
                nextURL = "http://" + siteName + nextURL

            web_cotent = urllib.urlopen(nextURL) # open website
            content = web_cotent.read()
            mc = re.findall('src="(.*?jpg)"', content) # old pattern: http.//[^ ]*?jpg

            print("next page")

        except:
            nextURL = False

    print("")
    print("download completed...")

if __name__ == "__main__":
    initial()
    downPic()

    try:
        input()
    except:
        pass



