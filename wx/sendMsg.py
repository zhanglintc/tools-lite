#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, urllib2
import json
import requests

tokenFile = "AccessToken"

sAppId = "wx1c77202393c1c41d"
secret = "3AhT8A1akqYHKVuLCtrcx3OvZPFHbMO03vvBaGu4xyciG8Lj6z1OGs8Zp-81ZtnE"

def getToken():
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={0}&corpsecret={1}".format(sAppId, secret)

    web = urllib.urlopen(url)
    ret = json.loads(web.read())
    access_token = ret["access_token"]

    # write token to local file
    fw = open(tokenFile, "wb")
    fw.write(access_token)
    fw.close()

    return access_token

def sendMsg(content = ""):
    try:
        fr = open(tokenFile, "rb")
        access_token = fr.read().strip()

    except:
        access_token = getToken()
   
    params = {
        "touser" : "@all",
        "toparty": "@all",
        "totag"  : "@all",
        "agentid": "0",   # str or int is OK
        "msgtype": "text",
        "text": {
            "content": content or "test message"
            },
        }
    params = json.dumps(params, ensure_ascii = False)

    resp = requests.post("https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={0}".format(access_token), data = params).text
    print "from sendMsg: " + resp
    resp = json.loads(resp)
    if resp["errcode"] != 0:
        print "from sendMsg: " + "Error {0}: {1}".format(resp["errcode"], resp["errmsg"])

        if resp["errcode"] == 42001 or resp["errcode"] == 40014:
            access_token = getToken()
            print "from sendMsg: " + requests.post("https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={0}".format(access_token), data = params).text


if __name__ == '__main__':
    sendMsg()
