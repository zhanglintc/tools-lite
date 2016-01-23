#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import json
import os

import python_send

PASSWORD = None

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
    PASSWORD = "YOURPASSWORD"
else:
    pass

SENDFROM = "zhanglintc@163.com"
USERNAME = "zhanglintc@163.com"
SMTPSERV = "smtp.163.com"
MailList = [
    "zhanglintc623@foxmail.com",
]

city = "harbin"
city_CN = "哈尔滨"
base_url = "http://api.worldweatheronline.com/free/v2/weather.ashx"
params = "?key=55f1fdd05fba23be0a18043d0a017&num_of_days=3&format=json&lang=zh&q={0}".format(city)

resp = urllib.urlopen(base_url + params)
dikt = json.loads(resp.read())

date = dikt['data']['weather'][0]['date']
morning =  dikt['data']['weather'][0]['hourly'][2]
noon = dikt['data']['weather'][0]['hourly'][4]
afternoon = dikt['data']['weather'][0]['hourly'][6]

morning_tempC, morning_Desc = morning['tempC'], morning['lang_zh'][0]['value'].encode("utf-8")
noon_tempC, noon_Desc = noon['tempC'], noon['lang_zh'][0]['value'].encode("utf-8")
afternoon_tempC, afternoon_Desc = afternoon['tempC'], afternoon['lang_zh'][0]['value'].encode("utf-8")

today = """\
{city_CN} {date} 天气状况:
早上 {morning_tempC} 摄氏度, {morning_Desc}.
中午 {noon_tempC} 摄氏度, {noon_Desc}.
晚上 {afternoon_tempC} 摄氏度, {afternoon_Desc}.\
""".format(
    city_CN = city_CN,
    date = date,
    morning_tempC = morning_tempC,
    morning_Desc = morning_Desc,
    noon_tempC = noon_tempC,
    noon_Desc = noon_Desc,
    afternoon_tempC = afternoon_tempC,
    afternoon_Desc = afternoon_Desc,
)

try:
    fr = open("yesterday.txt", "rb")
    yesterday = fr.read()
    fr.close
except:
    yesterday = ""

fw = open("yesterday.txt", "wb")
fw.write(today)
fw.close

mail_content = "{0}\n\n{1}".format(today, yesterday)

python_send.sendEmail(
    to_addr = MailList,
    from_addr = SENDFROM,
    alias = "Lane-Aliyun",
    password = PASSWORD,
    smtp_server = SMTPSERV,
    subject = "{0}天气状况".format(city_CN),
    content = mail_content
)


