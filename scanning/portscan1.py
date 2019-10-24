#!/usr/bin/python

# import socket library to help us scan for ports
import socket

# creating a socket object and assigning it to sock, 
# and we are going to use the AF_INET which says it is going
# to be an IPv4 address host that we are going to connect to 
# and the SOCK_STREAM represents we are going to use TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# what is the host to connect to
host = "10.64.240.173"
# what is the port you want to scan
port = 111 


def portscanner(port):
    if sock.connect_ex((host,port)):
        print "port %d is closed" % (port)
    else:
        print "port %d is opened" % (port)

portscanner(port);
