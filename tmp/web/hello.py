#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cgi import parse_qs, escape
from WXBizMsgCrypt import WXBizMsgCrypt

sToken          = "c8tcRUW1j"
sEncodingAESKey = "e6msYFTXeev0zxFNQpNCzq91SfzcAKBBn3CGXAJgd90"
sAppId          = "wx1c77202393c1c41d"

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])

    # print "PATH_INFO: ", environ['PATH_INFO']
    # print "QUERY_STRING: ", environ['QUERY_STRING']
    # print "REQUEST_METHOD: ", environ['REQUEST_METHOD']

    d = parse_qs(environ['QUERY_STRING'])
    print d

    wxDecrypt = WXBizMsgCrypt(sToken, sEncodingAESKey, sAppId)
    ret ,decryp_xml = wxDecrypt.DecryptMsg(d["echostr"], d["msg_signature"], d["timestamp"], d["nonce"])

    print "No.1: ", ret
    print "No.2: ", decryp_xml

    return decryp_xml or "hello world"
