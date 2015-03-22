import urllib
import os, re

LOG_FILE = "leetcode.log"
WEB_URL = "https://github.com/zhanglintc/tools-lite/tree/master/leetcode/python"

STATUS = {
    "INIT": [],
    "MIDDLE": [],
    "AC": [],
}

site = urllib.urlopen(WEB_URL)
content = site.read()

fw = open(LOG_FILE, "wb")
fw.write(content)
fw.close()

fr = open(LOG_FILE, "rb")

flag = "end" # can be set as "start" or "end"
line = True
while line:
    line = fr.readline()
    # start to scan
    if "tbody" in line and flag == "end":
        flag = "start"

    # end of scan
    elif "tbody" in line and flag == "start":
        flag = "end"

    # scan
    if flag == "start":
        mc = re.search('title=".*', line)

        # get file name
        if mc and ".py" in mc.group():
            file_name = re.search('title="(.*?)"', mc.group()).group(1)

        if mc and "INIT" in mc.group():
            STATUS["INIT"].append(file_name)

        if mc and "MIDDLE" in mc.group():
            STATUS["MIDDLE"].append(file_name)

        if mc and "AC" in mc.group():
            STATUS["AC"].append(file_name)

fr.close()
os.remove(LOG_FILE)


# print the final result
for file_name in STATUS["INIT"]:
    print("INIT: {}".format(file_name))

for file_name in STATUS["MIDDLE"]:
    print("MIDDLE: {}".format(file_name))


