#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cgi import parse_qs, escape
from encrypt.WXBizMsgCrypt import WXBizMsgCrypt
from tools.getCommit import getCommit

import urllib, urllib2
import json
import requests

# disable warnings
import warnings
warnings.filterwarnings("ignore")

sToken          = "c8tcRUW1j"
sEncodingAESKey = "e6msYFTXeev0zxFNQpNCzq91SfzcAKBBn3CGXAJgd90"
sAppId          = "wx1c77202393c1c41d"

# {0}: ToUserName
# {1}: FromUserName
# {2}: CreateTime
# {3}: Content
text_T = "\
<xml>\
<ToUserName><![CDATA[zhanglintc]]></ToUserName>\
<FromUserName><![CDATA[wx1c77202393c1c41d]]></FromUserName>\
<CreateTime>1348831860</CreateTime>\
<MsgType><![CDATA[text]]></MsgType>\
<Content><![CDATA[{0}]]></Content>\
</xml>\
"

def getRequestBody(environ):
    # the environment variable CONTENT_LENGTH may be empty or missing
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))

    except (ValueError):
        request_body_size = 0

    # When the method is POST the query string will be sent
    # in the HTTP request body which is passed by the WSGI server
    # in the file like wsgi.input environment variable.
    request_body = environ['wsgi.input'].read(request_body_size)

    return request_body

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])

    request_body = getRequestBody(environ)

    d = parse_qs(environ['QUERY_STRING'])

    wxDecrypt = WXBizMsgCrypt(sToken, sEncodingAESKey, sAppId)
    ret, xml_content = wxDecrypt.DecryptMsg(request_body, d["msg_signature"][0], d["timestamp"][0], d["nonce"][0])

    sReplyEchoStr = ""
    if "echostr" in environ['QUERY_STRING']:
        d = parse_qs(environ['QUERY_STRING'])

        wxDecrypt = WXBizMsgCrypt(sToken, sEncodingAESKey, sAppId)
        ret ,sReplyEchoStr = wxDecrypt.VerifyURL(d["msg_signature"][0], d["timestamp"][0], d["nonce"][0], d["echostr"][0])

    # return sReplyEchoStr or "hello world"
    ret, message = wxDecrypt.EncryptMsg(text_T.format(getCommit("https://github.com/zhanglintc?period=daily")), d["nonce"][0])
    return message or "hello world"

def sendSth():
    secret = "3AhT8A1akqYHKVuLCtrcx3OvZPFHbMO03vvBaGu4xyciG8Lj6z1OGs8Zp-81ZtnE"
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={0}&corpsecret={1}".format(sAppId, secret)
    access_token = ""
    if not access_token:
        web = urllib.urlopen(url)
        ret = json.loads(web.read())
        access_token = ret["access_token"]
        print access_token

    params = {
        "button":[
            {    
                "name":"小工具",
                "key":"V1001_TOOL_LITE",
                "sub_button":[
                    {
                        "type":"view",
                        "name":"soso搜索",
                        "url":"http://www.soso.com/"
                    },
                    {
                        "type":"click",
                        "name":"Github报告",
                        "key":"V1001_GITHUB"
                    },
                ]
            },
            {
                "name":"关于",
                "sub_button":[
                    {
                        "type":"view",
                        "name":"打开主页",
                        "url":"http://zhanglintc.co/"
                    },
                    {
                        "type":"view",
                        "name":"打开博客",
                        "url":"http://imlane.farbox.com"
                    },
                ]
            }
        ]
    }
    params = json.dumps(params, ensure_ascii = False)
    print params

    print requests.post("https://qyapi.weixin.qq.com/cgi-bin/menu/create?access_token={0}&agentid=0".format(access_token), data = params).text

def main():
    sendSth()
    # getCommit("https://github.com/zhanglintc?period=daily")
    pass

if __name__ == '__main__':
    main()
