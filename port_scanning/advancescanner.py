#!/usr/bin/python

# to syntax check run
# python -m py_compile <filename>

from socket import *
# library below will allow us to specify
# help options that will get prompted for the user
import optparse
from threading import *


def connScan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print("%d/tcp Open" % tgtPort)
    except:
        print("%d/tcp Closed" % tgtPort)
    finally:
        sock.close()


def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('Unknown host %s' % tgtHost)
    try:
        tgtName = gethostbyaddr(tgtIP)
        print("Scan results for: " + tgtName[0])
    except:
        print('Scan results for: ' + tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        # create a thread to check for ports available in the host
        # target= the function
        # args= the arguments to be passed into the function
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()


def main():
    # this will help the user understand how to use the program
    parser = optparse.OptionParser('Usage of program: ' + '-H <target host> -p <target ports>')
    # the add_option is a method which helps specify different 
    # setting for the program
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPorts', type='string', help='specify target ports seperated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    # because we have said they are allowed multiple ports
    # we are going to split the string from the commas
    tgtPorts = str(options.tgtPorts).split(',')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost, tgtPorts)


if __name__ == '__main__':
    main()

# To call this program
# python advancescanner.py -H 192.168.1.10 -p 8,10
# python advancescanner.py -H google.com -p 443,8080,92
# python advancescanner.py -H 18.90.23.54 -p 330
# python advancescanner.py -H bbc.co.uk -p 443
