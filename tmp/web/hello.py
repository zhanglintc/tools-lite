#!/usr/bin/env python
# -*- coding: utf-8 -*-

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    print environ['PATH_INFO']
    return 'Hello, web!'