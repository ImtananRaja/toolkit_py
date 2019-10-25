#!/usr/bin/python

from socket import *
# library below will allow us to specify
# help options that will get prompted for the user
import optparse
from threading import *

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
        print parser.usage
        exit(0)
    #portScan(tgtHost, tgtPorts)

main()

