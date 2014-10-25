#!/usr/bin/env python
import Logging
import urllib2
import sys
import re
__author__ = 'Jared Stroud', 'Andrew Garbutt'


class Request:
    ''' Requests class handles receiving information from umadbro website'''

    def __init__(self):
        self.req_log = Logging.Loggy()

    # Name: make_request
    # Param: self, user command
    # Purpose: Making request to "umadbro" server based on user args.
    # Return: Nothing.
    def make_request(self, command):

            if command == "list":
                self.list_tools()
            else:
                try:
                    req = urllib2.urlopen('http://umadbro.pw/pages/'+str(command))

                    if req.getcode() == 200:  # File exists.
                        html = req.read()
                        print(html)
						
                except urllib2.HTTPError as conn_error:
			print("[-] Error!!\n\t" + str(conn_error) + 
			"\n\tWe'll try to add the page you requested soon!")
			self.req_log.log(str(command))
			self.req_log.post_log() #Sending error log to umadbro.pw
			self.req_log.close()
					print("[-] Error!!\n\t" + str(conn_error) + 
					"\n\tWe'll try to add the page you requested soon!")
					self.req_log.log(str(command))
					self.req_log.post_log()

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

    # Author: Andrew Garbutt
    # Name: list_tools
    # Param: none
    # Purpose:  check current available online tool pages.
    # Return: none.
    def list_tools(self ):
        url = 'http://www.umadbro.pw/pages/'
        response = urllib2.urlopen(url)
        html = response.read()

        #Parse source code to find links
        links = re.findall('href=[a-z\"A-Z0-9]+\"', html)

        #Print out just the name of the commands
        for cur_link in links:
            end_substr_len = (len(cur_link) - 1)
            print cur_link[6:end_substr_len]
