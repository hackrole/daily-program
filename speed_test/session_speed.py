#!/usr/bin/env python
# encoding: utf-8

import time
import json
import requests
from requests import Request, Session


client_id = "YXA6W2FyYL-7EeSWmMOJcIp39A"
client_secret = "YXA6RweECgwCQ3cbZoTdwzYAeTfOHEo"

headers = {
    "Content-Type": "application/json",
}


def session_speed():
    session = Session()
    session.headers.update({"Content-Type": "application/json"})

    start = time.time()

    url = "https://a1.easemob.com/joygin/pengqiaotest/token"
    data = {"grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret}
    req1 = Request("POST", url, data=json.dumps(data))

    resp = session.send(session.prepare_request(req1))

    token = json.loads(resp.content)
    headers = {
        'Authorization': "Bearer %s" % token['access_token'],
    }

    for i in range(10):
        url = "https://a1.easemob.com/joygin/pengqiaotest/users"
        data = {
            "username": "user_%s" % i,
            "password": '123456',
            "nickname": "nick_%s" % i,
        }
        req = Request("POST", url, data=json.dumps(data),
                      headers=headers)

        resp = session.send(session.prepare_request(req))

    url = "https://a1.easemob.com/joygin/pengqiaotest/users?limit=20"
    req = Request("DELETE", url, headers=headers)
    resp = session.send(session.prepare_request(req))

    end = time.time()
    print "session time:", end - start


def raw_send():
    start = time.time()

    headers = {
        "Content-Type": "application/json",
    }

    url = "https://a1.easemob.com/joygin/pengqiaotest/token"
    data = {"grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret}

    resp = requests.post(url, data=json.dumps(data), headers=headers)

    token = json.loads(resp.content)
    headers.update({'Authorization': "Bearer %s" % token['access_token']})

    for i in range(10):
        url = "https://a1.easemob.com/joygin/pengqiaotest/users"
        data = {
            "username": "user_%s" % i,
            "password": '123456',
            "nickname": "nick_%s" % i,
        }
        resp = requests.post(url, data=json.dumps(data), headers=headers)

    url = "https://a1.easemob.com/joygin/pengqiaotest/users?limit=20"
    resp = requests.delete(url, headers=headers)

    end = time.time()
    print "raw time:", end - start


session_speed()
raw_send()
