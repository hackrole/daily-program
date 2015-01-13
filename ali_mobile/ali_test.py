#!/usr/bin/env python
# encoding: utf-8

import json
import mock
import utils
from unittest2 import TestCase


class InfoTest(TestCase):
    def test_quick_order_return_quick(self):
        url = "/get_info"
        data = {
            'sessionid': self.session.session_key,
        }

        response = self.client.get(url, data)
        dut = json.loads(response.content)

        self.assertEquals(response.status_code, 200)
        self.assertTrue(dut['success'])
        self.assertIn("/api1/alis/quick_notify_callback",
                      dut['data']['info_str'])


class CallbackTest(TestCase):

    def test_return_ok(self):

        url = "/callback"
        data = {
            'out_trade_no': "dddd",
            'trade_status': 'TRADE_FINISHED',
            'total_fee': '20',
        }

        with mock.patch('verify_callback') as MockClass:
            MockClass.return_value = True

            response = self.client.post(url, data)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, 'success')


class MakeInfoTest(TestCase):

    def test_make_info_not_raise_exception(self):
        trade_no = "trade_no_224"
        subject = "test_make_info"
        body = "test the make info not raise"
        total_fee = 12.00
        show_url = "http://www.showme.com"

        dut = utils.make_info(trade_no, subject, body, total_fee, show_url)
        self.assertIsNotNone(dut)
