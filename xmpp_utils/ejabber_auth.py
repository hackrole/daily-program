#!/usr/bin/env python
# encoding: utf-8

u"""
用户ejabberd聊天服务器的外部认证脚本.
"""

import sys
import logging
import struct
from mongoengine import connect
#from sell_time import models


connect('nchat_dev')


def from_ejabberd():
    input_length = sys.stdin.read(2)
    logging.info("Bytes read: %s" % len(input_length))
    logging.info("Input lenght: %s" % input_length)
    (size,) = struct.unpack('>h', input_length)
    return sys.stdin.read(size).split(':')


def to_ejabberd(success):
    answer = 0
    if success:
        answer = 1

    token = struct.pack('>hh', 2, answer)
    sys.stdout.write(token)
    sys.stdout.flush()


def auth(mobile, server, password):
    return True


def isuser(mobile, server):
    return True


def setpass(mobile, server, password):
    return False


while True:
    data = from_ejabberd()
    success = False
    logging.info(data)
    if data[0] == "auth":
        success = auth(data[1], data[2], data[3])
    elif data[0] == "isuser":
        success = isuser(data[1], data[2])
    elif data[0] == "setpass":
        success = setpass(data[1], data[2], data[3])

    msg = "data: %s with result: %s" % (data, success)
    logging.info(msg)
    to_ejabberd(success)
