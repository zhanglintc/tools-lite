#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cgi import parse_qs, escape
from WXBizMsgCrypt import WXBizMsgCrypt
from urllib import unquote
import urllib, urllib2
import json
import requests

sToken          = "c8tcRUW1j"
sEncodingAESKey = "e6msYFTXeev0zxFNQpNCzq91SfzcAKBBn3CGXAJgd90"
sAppId          = "wx1c77202393c1c41d"

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])

    # print "PATH_INFO: ", environ['PATH_INFO']
    # print "QUERY_STRING: ", environ['QUERY_STRING']
    # print "REQUEST_METHOD: ", environ['REQUEST_METHOD']

    sReplyEchoStr = ""
    if "echostr" in environ['QUERY_STRING']:
        # d = parse_qs(unquote(environ['QUERY_STRING']))
        d = parse_qs(environ['QUERY_STRING'])
        # print d

        wxDecrypt = WXBizMsgCrypt(sToken, sEncodingAESKey, sAppId)
        ret ,sReplyEchoStr = wxDecrypt.VerifyURL(d["msg_signature"][0], d["timestamp"][0], d["nonce"][0], d["echostr"][0])

        print "No.1: ", ret
        print "No.2: ", sReplyEchoStr

    return sReplyEchoStr or "hello world"

def main():
    secret = "3AhT8A1akqYHKVuLCtrcx3OvZPFHbMO03vvBaGu4xyciG8Lj6z1OGs8Zp-81ZtnE"
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={0}&corpsecret={1}".format(sAppId, secret)
    access_token = ""
    if not access_token:
        web = urllib.urlopen(url)
        ret = json.loads(web.read())
        access_token = ret["access_token"]
        print access_token

    params = {
        "touser": "@all",
        "toparty": "@all",
        "totag": "@all",
        "agentid": "0", # str or int is OK
        "msgtype": "text",
        "text": {
            "content": "test message"
            },
        }
    params = json.dumps(params, ensure_ascii = False)
    print params

    print requests.post("https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(access_token), data = params).text

if __name__ == '__main__':
    main()
