#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import *
import os.path
import sys

target = ('115.29.192.240', 8988)

def get_header(name):
    leng = len(name)
    assert leng < 250
    return chr(leng) + name

def send_file(name):
    basename = os.path.basename(name)
    header = get_header(basename)
    cont = open(name, "rb").read()
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(target)
    s.sendall(header)
    s.sendall(cont)
    s.close()

while True:
    f = raw_input("Drag file here: ")
    try:
        send_file(f)
        print 'Success: "%s" has been sent to server.\n' % os.path.basename(f)
    except:
        print "Error: File send has failed.\n"
