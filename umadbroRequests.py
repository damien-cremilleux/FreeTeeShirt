#!/usr/bin/env python
import urllib
__author__ = 'jared'


class Request:
    ''' Requests class handles receiving information from umadbro website'''

    def __init__(self):
        print("Successfully created object!")

    def make_request(self, command):

        req = urllib.urlopen('http://umadbro.pw/'+str(command))

        if req.getcode() != 200: # File doesn't exist
            print("Error! that page doesn't exist! (yet!)")
        else:
            print(req)



