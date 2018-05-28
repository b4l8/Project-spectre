#! /usr/bin/env python

import socket

s = socket.socket()

host = socket.gethostname()
port = 13000
s.connect((host,port))

print s.recv(1024)

