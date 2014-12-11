#!/usr/bin/env python
# encoding: utf-8

import json
import uuid
import gevent
import os
from gevent import monkey
from gevent import queue

monkey.patch_all()


fp = "../btshare.json"
f = open(fp)
data = json.load(f)


q = queue.JoinableQueue()

for i in data:
    d = {
        'bt_url': i['bt_url'],
        'title': str(uuid.uuid1()),
    }
    q.put(d)


def worker():
    while True:
        item = q.get()
        try:
            fn = '.'.join([item['title'], "torrent"])
            os.system('wget "%s" -O %s' % (item['bt_url'], fn))
        finally:
            q.task_done()


for i in range(20):
    gevent.spawn(worker)

q.join()
