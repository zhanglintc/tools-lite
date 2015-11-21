#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, re, os
import python_send

# mail setting
SENDFROM = "zhanglintc@163.com"
USERNAME = "zhanglintc@163.com"
SMTPSERV = "smtp.163.com"
PASSWORD = None
MAILLIST = [
    "zhanglintc623@foxmail.com",
]

# try to get password in your user folder
try:
    with open(os.path.expanduser('~') + '/.smpass', 'rb') as fr:
        PASSWORD = fr.read().strip()
except:
    pass

# if failed, try to get password in the script's folder
if not PASSWORD:
    try:
        with open(sys.path[0] + '/.smpass', 'rb') as fr:
            PASSWORD = fr.read().strip()
    except:
        pass

# if still failed, use password in the script
if not PASSWORD:
    PASSWORD = "YOURPASSWORD~"
else:
    pass

def main():
    web = urllib.urlopen("http://news.sina.com.cn/hotnews/?from=faxian_xinwen&mod=hot")
    res = web.read()

    mc = re.search("seo内容输出开始.*seo内容输出结束", res, re.DOTALL)
    rank = mc.group(0)

    mc = re.search("<table.*?table>", rank, re.DOTALL)
    topHit = mc.group()

    newsList = re.findall("<td>\d</td>.*a href='(.*)' target='_blank'>(.*)</a></td><td>", topHit)
    sendContent = ""
    for news in newsList:
        sendContent += "{0}:\n{1}\n\n".format(news[1], news[0])

    # # debug use only
    # print sendContent

    # send email
    if True: # debug switcher
        python_send.sendEmail(
            to_addr = MAILLIST,
            from_addr = SENDFROM,
            alias = "sina news rss",
            password = PASSWORD,
            smtp_server = SMTPSERV,
            subject = "每日热点新闻",
            content = sendContent,
        )

if __name__ == '__main__':
    main()
