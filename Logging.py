#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Jared Stroud', 'Andrew Garbutt'
import urllib2
import platform
import tempfile

class Loggy:

    def __init__(self):  # Creation of log file when object is made.
		self.log_file = open(tempfile.gettempdir() + '/umadbro.log', "a+")
		self.close()

    # Name: log
    # Purpose: Log commands for debugging purposes.
    # Param: str(command) that's attempting to be executed
    # Return: Nothing
    def log(self, command):
		self.log_file = open(tempfile.gettempdir() + '/umadbro.log', "a+")
		self.log_file.write(command + "\n")
		self.close()

    # Name: post_log
    # Purpose: send an HTTP PUT message to umadbro server
    #          to figure out what aren't working and docs to add.
    # Return: Nothing
    def post_log(self):
		self.log_file = open(tempfile.gettempdir() + '/umadbro.log', "r")
		tmp_contents = self.log_file.read()
		opener = urllib2.build_opener(urllib2.HTTPHandler)
		request = urllib2.Request('http://umadbro.pw', str(tmp_contents))
		request.add_header('Content-Type', 'text/umad_requests')
		request.get_method = 'PUT'
		self.close()

    # name: close
    # Purpose: close file after writing/reading has occurred.
    # Return: Nothing
    def close(self):  # Cleaning up the file
        self.log_file.close()
