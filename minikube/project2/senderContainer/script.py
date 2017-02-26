#!/usr/bin/python
# -*- encoding: utf-8 -*-
import socket
import time
import sys

print sys.argv[1]
print sys.argv[2]


for i in range(1,10):
	time.sleep(2)
	data = "My parameters that I want to share with the server on ith iteration %d" % (i)
	print "sedning data: %d" % (i)
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((sys.argv[1], int(sys.argv[2])))
	sock.sendall(data)
	sock.close()

