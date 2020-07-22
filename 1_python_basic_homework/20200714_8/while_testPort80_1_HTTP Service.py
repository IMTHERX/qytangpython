#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# qytang Python V4
# WangTao
# 简易的HTTP80端口
from http.server import HTTPServer,CGIHTTPRequestHandler
prot = 80
httpd = HTTPServer(('',prot),CGIHTTPRequestHandler)
print('Starting simple httpd on port:' + str(httpd.server_port))
httpd.serve_forever()
