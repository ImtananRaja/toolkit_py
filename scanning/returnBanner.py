#!/usr/bin/python

import socket

# to syntax check run
# python -m py_compile <filename>

def returnbanner(ip, port):
    try:
        # timeout if no response in 2 seconds
        socket.setdefaulttimeout(2)
        # create a socket object
        s = socket.socket()
        # connect to the ip and port
        s.connect((ip, port))
        # what we receive from the host when we scan
        # and the number of bytes to receive
        banner = s.recv(1024)
        return banner
    except:
        return


def main():
    ip = raw_input("Enter target IP: ")
    for port in range(1, 100):
        banner = returnbanner(ip, port)
        if banner:
            print "[+] " + ip + "on Port " + str(port) + " : " + banner


if __name__ == '__main__':
    main()

# for metasploitable machine
# ip = 10.64.240.204
# port = 22
# response is [+] 10.64.240.204: SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1
# you can use the 'SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1'
# and search for exploits/vunerbilities

