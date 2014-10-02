#!/usr/bin/env python
import sys, requests
__author__ = 'jared'


class Request:
    ''' Requests class handles receiving information from umadbro website'''

    def __init__(self):
        print("Successfully created object!")

    def make_request(self, command):

        req = requests.get('http://104.131.22.131/'+str(command), stream=True)

        if req.status_code != 200:
            print("Error! that page doesn't exist!")
        else:
            print(req.raw.read())

