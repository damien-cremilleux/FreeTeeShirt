#!/usr/bin/env python
import urllib2, sys
__author__ = 'Jared Stroud'

class Request:
    ''' Requests class handles receiving information from umadbro website'''

    def __init__(self):
        print("Successfully created object!")

    # Name: make_request
    # Param: self, user command
    # Purpose: Making request to "umadbro" server based on user args.
    # Return: Nothing.
    def make_request(self, command):

            try:
                req = urllib2.urlopen('http://umadbro.pw/'+str(command))
                if req.getcode() != 200: # File doesn't exist
                    print("Error! that page doesn't exist! (yet!)\n")
                    sys.exit()
                else:
                   html = req.read()
                   print(html)
            except urllib2.HTTPError as conn_error:
                print("[-] Error!!\n\t" + str(conn_error))

    # Name: check_args
    # Param: self, command line arguments
    # Purpose: Checking the user passed in tools to search.
    #          Script exits if nothing is found.
    # Return: Array of searchable items
    def check_args(self, usr_arg):
        arg_len = len(sys.argv)
        if arg_len == 0:
            print("Error! please enter an tool! Ex: umadbro 'toolname' ")
            sys.exit()
        else:
            return [usr_arg]