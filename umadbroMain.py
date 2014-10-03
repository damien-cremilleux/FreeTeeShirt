#!/usr/bin/env python
__author__ = 'jared'

import umadbroRequests, sys

madRequest = umadbroRequests.Request()

madRequest.make_request(sys.argv[1])