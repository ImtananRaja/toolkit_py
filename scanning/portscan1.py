#!/usr/bin/python

# import socket library to help us scan for ports
import socket
# the import below is python3 and above
from termcolor import colored

# creating a socket object and assigning it to sock, 
# and we are going to use the AF_INET which says it is going
# to be an IPv4 address host that we are going to connect to 
# and the SOCK_STREAM represents we are going to use TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# give a 'false' value back after 3 seconds if no response 
# is recieved from the ip/port
socket.setdefaulttimeout(3)

# what is the host to connect to
#host = "10.64.240.173"
# what is the port you want to scan
#port = 111 

# get user input instead of hard coding the IP or the port
# raw_input for python2 and input for python3
host = input("Please type the IP address you want to scan: ")

# we have to wrap it in an int because it is going to be pure numbers
# that the sock.connect_ex is going to do
#port = int(raw_input("Please type the port you want to scan: "))

def portscanner(port):
    if sock.connect_ex((host,port)):
        # adding colours so we can see the difference
        print(colored("port %d is closed" % (port), 'red'))
    else:
        print(colored("port %d is open" % (port), 'green'))

# scanning the first 1000 ports for the
# give ip address
for port in range(1, 1000):
    portscanner(port);
