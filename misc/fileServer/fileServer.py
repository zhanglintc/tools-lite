#!/usr/bin/env python
# -*- coding: utf-8 -*-

import SocketServer, os

# Format: name_len      --- one byte
#         name          --- name_len bytes
#         data          --- variable length

# Save data to name into current directory
# Refer to: http://blog.csdn.net/g__gle/article/details/8144968
addr = ('', 8988)
class MyTCPHandler (SocketServer.StreamRequestHandler):
    def handle(self):
        name_len = ord(self.rfile.read(1))
        name = self.rfile.read(name_len)
        print "Get request: %s" % name
        fd = open(name, 'wb')
        cont = self.rfile.read(4096)    
        while cont:
            fd.write(cont)
            cont = self.rfile.read(4096)
        fd.close()
        print "Out: %s" % name
        os.system("sudo mv ./{0} /usr/local/tomcat/server/webapps/".format(name))
        print "Move: %s" % name

server = SocketServer.TCPServer(addr, MyTCPHandler)
print "Serving on port %s ..." % addr[1]
server.serve_forever()
