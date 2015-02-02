# coding = utf-8

import os, re
import urllib
import subprocess

# mailto = "zhanglintc623@foxmail.com"
mailto = "349655336@qq.com"

def sendmail(type):
    if type == "bingo":
        send_content = "11.1 inches MacBook Air available now\nPlease check official site as soon as possible\nBuy now!!!"
        send_command = 'echo "{0}" | mutt -s "Buy Now!!! MacBook Air Available!!!" {1}'.format(send_content, mailto)

        sp = subprocess.Popen(["/bin/bash", "-i", "-c", send_command])
        sp.communicate()

    elif type == "normal":
        send_content = "this is hourly report\n11.1 inches MacBook Air is NOT available right now\nwe'll continue monitoring"
        send_command = 'echo "{0}" | mutt -s "Mac Price Hourly Report" {1}'.format(send_content, mailto)

        sp = subprocess.Popen(["/bin/bash", "-i", "-c", send_command])
        sp.communicate()

    else:
        pass

count = '0'

with open("/home/lane/tools-lite/python/MacCnt.txt", "ab") as fa:
    pass

with open("/home/lane/tools-lite/python/MacCnt.txt", "rb") as fr:
    read = fr.read()
    if not read:
        count = '0'
    elif int(read) % 120 == 0:
        print("normal")
        count = str(int(read) + 1)
        sendmail("normal")
    else:
        count = str(int(read) + 1)

with open("/home/lane/tools-lite/python/MacCnt.txt", "wb") as fw:
    fw.write(count)

recv = urllib.urlopen("http://store.apple.com/hk-zh/browse/home/specialdeals/mac")
recv = urllib.urlopen("http://store.apple.com/hk-zh/browse/home/specialdeals/mac")
content = recv.read()

p = re.compile("HK\$.*")
matches = p.findall(content)
prices = []
for match in matches:
    match = match.replace("HK$", "")
    match = match.replace(",", "")
    prices.append(int(match))

for price in prices:
    if 5000 < price < 6000:
        print("bingo")
        sendmail("bingo")
    else:
        print("not target")
