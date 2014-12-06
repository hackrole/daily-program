#!/usr/bin/env python
# encoding: utf-8

import json
from os import path


fp = path.join(
    path.dirname(path.realpath(__file__)),
    "btshare.json"
)

text = open(fp).read()
json.loads(text)
