#!/usr/bin/env python
# encoding: utf-8

import json
import jinja2


a = json.load(open("../btshare.json"))

t = open("../t1.html").read()
p = jinja2.Template(t.decode('utf8'))

s = p.render(divs=a)

f = open("../tt2.html", 'w')
f.write(s.encode('utf8'))
f.flush()
