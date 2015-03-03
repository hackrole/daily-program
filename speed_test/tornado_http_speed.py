#!/usr/bin/env python
# encoding: utf-8

import timeit
import time
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient


io = IOLoop.instance()
url = "http://www.easemob.com/hx/index.html"


@gen.coroutine
def simple_speed():
    client = AsyncHTTPClient()
    for i in range(5):
        yield client.fetch(url)


@gen.coroutine
def curl_speed():
    AsyncHTTPClient.configure('tornado.curl_httpclient.CurlAsyncHTTPClient')
    client = AsyncHTTPClient()
    for i in range(5):
        yield client.fetch(url)

start = time.time()
print 'simple', simple_speed()
print 'end', time.time() - start


start = time.time()
print 'simple', curl_speed()
print 'end', time.time() - start

print "simple", timeit.repeat("io.run_sync(simple_speed, timeout=100000000)",
                              setup="from __main__ import simple_speed, io",
                              number=1)
print "curl", timeit.repeat("io.run_sync(curl_speed, timeout=1000000000)",
                            setup="from __main__ import curl_speed, io",
                            number=3)
