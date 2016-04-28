#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import *
import struct
import os.path
import sys

target = ('localhost', 8988)

def get_header(name):
    leng = len(name)
    assert leng < 250
    return chr(leng) + name

def send_file(name):
    basename = os.path.basename(name)
    header = get_header(basename)
    content = open(name, "rb").read()
    file_size = len(content)
    content = struct.pack(">l", file_size) + content
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(target)
    s.sendall(header)
    s.sendall(content)

    float_file_size = float(file_size)
    from_socket = s.recv(4)
    while from_socket:
        server_gotten = struct.unpack(">l", from_socket)[0]
        sys.stdout.write("{0}%\r".format('%0.2f' % (server_gotten / float_file_size * 100)))
        sys.stdout.flush()
        from_socket = s.recv(4)

    s.close()

while True:
    f = raw_input("Drag file here: ")
    try:
        send_file(f)
        print 'Success: "%s" has been sent to server.\n' % os.path.basename(f)
    except Exception, e:
        print 'Error: %s\n' % e
