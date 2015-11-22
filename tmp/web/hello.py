#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cgi import parse_qs, escape
from WXBizMsgCrypt import WXBizMsgCrypt
from urllib import unquote

# firstAuth = "msg_signature=a9ea3b39e262ec645082c5b205b073a3331bff7b&timestamp=1448207658&nonce=411183241&echostr=viq5YYu1KIg%2FxOsH54z3fNNJQCwTbwvHfUllyPAmbFejXGkQ0Ow838mDKL8FgHjIFWKIStZmdOPHXDfaG36%2BTQ%3D%3D"

sToken          = "c8tcRUW1j"
sEncodingAESKey = "e6msYFTXeev0zxFNQpNCzq91SfzcAKBBn3CGXAJgd90"
sAppId          = "wx1c77202393c1c41d"

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])

    # print "PATH_INFO: ", environ['PATH_INFO']
    # print "QUERY_STRING: ", environ['QUERY_STRING']
    # print "REQUEST_METHOD: ", environ['REQUEST_METHOD']

    decryp_xml = ""
    if "echostr" in environ['QUERY_STRING']:
        d = parse_qs(unquote(environ['QUERY_STRING']))
        print d

        wxDecrypt = WXBizMsgCrypt(sToken, sEncodingAESKey, sAppId)
        ret ,decryp_xml = wxDecrypt.DecryptMsg(d["echostr"], d["msg_signature"], d["timestamp"], d["nonce"])

        print "No.1: ", ret
        print "No.2: ", decryp_xml

    return decryp_xml or "hello world"
