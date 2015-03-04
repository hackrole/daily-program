#!/usr/bin/env python
# encoding: utf-8

u"""
问题1: 设置了过大的 timeout 导致int32溢出，最终ioloop timeout.

问题2: AsyncHTTPClient有缓存，必须在使用前调用configure, 未尝试使用force_instace参数
"""

import timeit
import tornado.simple_httpclient
import tornado.curl_httpclient
from tornado import gen
from tornado.ioloop import IOLoop


io = IOLoop.instance()
url = "http://www.easemob.com/hx/index.html"


@gen.coroutine
def simple_speed():
    client = tornado.simple_httpclient.SimpleAsyncHTTPClient()
    for i in range(5):
        yield client.fetch(url)


@gen.coroutine
def curl_speed():
    client = tornado.curl_httpclient.CurlAsyncHTTPClient()
    for i in range(5):
        yield client.fetch(url)


print "simple", timeit.repeat("io.run_sync(simple_speed, timeout=3600)",
                              setup="from __main__ import simple_speed, io",
                              number=3)
print "curl", timeit.repeat("io.run_sync(curl_speed, timeout=3600)",
                            setup="from __main__ import curl_speed, io",
                            number=3)
