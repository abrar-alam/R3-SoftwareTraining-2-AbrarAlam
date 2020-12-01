#!/usr/bin/env python

import socket
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 10
MESSAGE = "[0][255][0][255]"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.sendall(bytes(MESSAGE, "utf8"))
data = s.recv(BUFFER_SIZE)
s.close()

print ("received data:", data.decode())
