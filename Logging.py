#!/usr/bin/env python
__author__ = 'jared'
import urllib2

class Loggy:

    def __init__(self):  # Creation of log file when object is made.
        self.log_file = open("/tmp/umadbro.log", 'a+')

    # Name: log
    # Purpose: Log commands for debugging purposes.
    # Param: str(command) that's attempting to be executed
    # Return: Nothing
    def log(self, command):
        self.log_file.write(command + "\n")

    # Name: post_log
    # Purpose: send an HTTP PUT message to umadbro server
    #          to figure out what aren't working and docs to add.
    # Return: Nothing
    def post_log(self):
        tmp_contents = self.log_file.read("/tmp/umadbro.log")
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        request = urllib2.Request('http://umadbro.pw', data=tmp_contents)
        request.add_header('Content-Type', 'text/umad_requests')
        request.get_method = lambda: 'PUT'
        url = opener.open(request)

    # name: close
    # Purpose: close file after writing/reading has occurred.
    # Return: Nothing
    def close(self):  # Cleaning up the file
        self.log_file.close()