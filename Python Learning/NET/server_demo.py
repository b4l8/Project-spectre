#! /usr/bin/env python

# in python , most of the net program don't detail the sock process

# 2 socket , server & client 
# 3 argument :  socket.AF_INET, 
#               (socket.SOCK_STREAM / socket.SOCK_DGRAM)
#               protocole

# server : bind ---------> listen
# client : connect

import socket

s = socket.socket()

host = socket.gethostname()
port = 13000
s.bind((host,port))

s.listen(5)
while True:
    c, addr = s.accept()
    print 'got connection from',addr
    c.send('Thank you for connecting')
    c.close()

