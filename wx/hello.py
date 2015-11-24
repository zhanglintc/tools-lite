#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cgi import parse_qs, escape
from WXBizMsgCrypt import WXBizMsgCrypt
from urllib import unquote
import urllib, urllib2
import json
import requests

# firstAuth = "msg_signature=a9ea3b39e262ec645082c5b205b073a3331bff7b&timestamp=1448207658&nonce=411183241&echostr=viq5YYu1KIg%2FxOsH54z3fNNJQCwTbwvHfUllyPAmbFejXGkQ0Ow838mDKL8FgHjIFWKIStZmdOPHXDfaG36%2BTQ%3D%3D"

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
    access_token = "GqVLzboUJyXs6G4El0L2GmkmhVmvNgiuO8s0y-jCppp7_6mWZ3BLCCOKog1FubNKqBL1EnkHczr94HyRQM8YDA"
    if not access_token:
        web = urllib.urlopen(url)
        ret = json.loads(web.read())
        access_token = ret["access_token"]
        print access_token

    params = urllib.urlencode({
        "agentid": "0",
        "msgtype": "text",
        "text": {
            "content": "test message"
            },
        "access_token": access_token
        })

    # request = urllib2.Request("https://qyapi.weixin.qq.com/cgi-bin/message/send", params)
    # print urllib2.urlopen(request).read()
    # requests.post("https://qyapi.weixin.qq.com/cgi-bin/message/send", data = params)

if __name__ == '__main__':
    main()
