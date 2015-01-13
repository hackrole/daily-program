#!/usr/bin/env python
# encoding: utf-8

import mock
import unittest
from sleekxmpp import ET
from loginBot import LoginBot
from friendBot import FriendBot
from sleekxmpp.test import TestSocket
from mongoengine import connect
from gevent.queue import Empty


class LoginBotTest(unittest.TestCase):

    def setUp(self):
        self.dbname = 'nchat_dev'
        self.db_client = connect(self.dbname)
        self.db_client.drop_database(self.dbname)

        self.jid = "test@localhost"
        self.pwd = "test"
        self.host = "localhost"
        self.bot = LoginBot(self.jid, self.pwd, self.host, self.dbname)
        self.bot.xmpp.set_socket(TestSocket())

        self.db = self.db_client[self.dbname]

    def tearDown(self):
        self.db_client.drop_database(self.dbname)

        del self.bot

    def test_login_renew_sessionid(self):
        self.assertEquals(self.old_session.status, 0)

        fjid = "18321445606@localhost"
        body = "mobile_token2"

        self.bot.login(fjid, body)

        # mesasge asserts
        msg = self.bot.xmpp.send_queue.get_nowait()
        self.assertIsNotNone(msg)
        self.assertTrue(isinstance(msg, basestring))

    def test_logout_close_session(self):
        self.assertEquals(self.old_session.status, 0)

        fjid = "18321445606@localhost"
        self.bot.logout(fjid)

        # mesasge asserts
        msg = self.bot.xmpp.send_queue.get_nowait()
        self.assertIsNotNone(msg)
        self.assertTrue(isinstance(msg, basestring))
        tjid = 'to="18321445606@localhost"'
        fjid = 'from="test@localhost"'
        self.assertNotEquals(msg.find(tjid), -1)
        self.assertNotEquals(msg.find(fjid), -1)

    def test_get_token_like_login(self):
        self.assertEquals(self.old_session.status, 0)

        fjid = "18321445606@localhost"
        body = "mobile_token2"
        self.bot.get_token(fjid, body)

        self.old_session.reload()
        self.assertEquals(self.old_session.status, 1)

        # mesasge asserts
        msg = self.bot.xmpp.send_queue.get_nowait()
        self.assertIsNotNone(msg)
        self.assertTrue(isinstance(msg, basestring))

    def test_message_nonchat_message_not_send(self):
        fjid = "18321445606@localhost"

        msg1 = self.bot.xmpp.Message(sto=self.jid, sfrom=fjid, stype='normal')
        msg2 = self.bot.xmpp.Message(sto=self.jid, sfrom=fjid,
                                     stype='grouchat')

        self.bot.message(msg1)
        with self.assertRaises(Empty):
            self.bot.xmpp.send_queue.get_nowait()

        self.bot.message(msg2)
        with self.assertRaises(Empty):
            self.bot.xmpp.send_queue.get_nowait()

    def test_message_nomobile_jid_not_send(self):
        fjid = "non-mobile@localhost"

        msg = self.bot.xmpp.Message(sto=self.jid, sfrom=fjid, stype='chat')

        self.bot.message(msg)
        with self.assertRaises(Empty):
            self.bot.xmpp.send_queue.get_nowait()

    def test_message_nonsubject_not_send(self):
        fjid = "18321445606@localhost"
        msg = self.bot.xmpp.Message(sto=self.jid, sfrom=fjid, stype='chat')
        msg['body'] = 'mobile-token'

        self.bot.message(msg)
        with self.assertRaises(Empty):
            self.bot.xmpp.send_queue.get_nowait()

    def test_message_error_subject_not_send(self):
        fjid = "18321445606@localhost"
        msg = self.bot.xmpp.Message(sto=self.jid, sfrom=fjid, stype='chat')
        msg['subject'] = 'not-login-or-logout'
        msg['body'] = 'mobile-token'

        self.bot.message(msg)
        with self.assertRaises(Empty):
            self.bot.xmpp.send_queue.get_nowait()

    def test_message_login_subject_login(self):
        fjid = "18321445606@localhost"
        msg = self.bot.xmpp.Message(sto=self.jid, sfrom=fjid, stype='chat')
        msg['subject'] = 'login'
        msg['body'] = 'mobile-token'

        with mock.patch.object(self.bot, 'login') as new_login:
            new_login.return_value = None
            self.bot.message(msg)
            self.assertEquals(new_login.call_count, 1)

    def test_message_logout_subject_logout(self):
        fjid = "18321445606@localhost"
        msg = self.bot.xmpp.Message(sto=self.jid, sfrom=fjid, stype='chat')
        msg['subject'] = 'logout'
        msg['body'] = 'mobile-token'

        with mock.patch.object(self.bot, 'logout') as new_logout:
            new_logout.return_value = None
            self.bot.message(msg)
            self.assertEquals(new_logout.call_count, 1)

        self.bot.message(msg)
        try:
            msg = self.bot.xmpp.send_queue.get_nowait()
            self.assertIsNotNone(msg)
        except Exception as e:
            print e.message
            self.fail('msg not send error')

    def test_message_get_token_subject_get_token(self):
        fjid = "18321445606@localhost"
        msg = self.bot.xmpp.Message(sto=self.jid, sfrom=fjid, stype='chat')
        msg['subject'] = 'get_token'
        msg['body'] = 'mobile-token'

        with mock.patch.object(self.bot, 'get_token') as new_get_token:
            new_get_token.return_value = None
            self.bot.message(msg)
            self.assertEquals(new_get_token.call_count, 1)


class FriendBotTest(unittest.TestCase):

    def db_init(self):
        u"""
        数据初始化
        """
        def create_default_user(mobile):
            pass

        def create_relation(master, guest, status):
            pass

        user_me = create_default_user("18321445606")
        user_w = create_default_user("18321445616")
        user_x = create_default_user("18321445626")
        user_f = create_default_user("18321445636")

        create_relation(user_me, user_w, 'both')
        create_relation(user_w, user_me, 'both')
        create_relation(user_me, user_x, 'asked')
        create_relation(user_x, user_me, 'ask')
        create_relation(user_me, user_f, 'black')
        create_relation(user_f, user_me, 'black')

    def setUp(self):
        self.dbname = "nchat_dev"
        self.db_client = connect(self.dbname)
        self.db_client.drop_database(self.dbname)
        self.db_init()

        self.jid = "friend.localhost"
        self.pwd = "joygin123"
        self.host = "127.0.0.1"
        self.port = "9098"
        self.bot = FriendBot(self.jid, self.pwd, self.host, self.port,
                             self.host, self.dbname)
        self.bot.xmpp.set_socket(TestSocket())

        self.db = self.db_client[self.dbname]

    def tearDown(self):
        self.db_client.drop_database(self.dbname)

        del self.bot

    def test_offline_presence_to_friends(self):
        pres = self.bot.xmpp.make_presence(pfrom="18321445606@localhost",
                                           pto="friend.localhost",
                                           ptype="unavailable")
        self.bot.user_offline(pres)

        dut_p1 = self.bot.xmpp.send_queue.get_nowait()
        self.assertIsNotNone(dut_p1)
        self.assertIn('from="18321445606@localhost"', dut_p1)
        self.assertIn('to="18321445616@localhost"', dut_p1)
        self.assertIn('type="unavailable"', dut_p1)

        with self.assertRaises(Empty):
            self.bot.xmpp.send_queue.get_nowait()

    def test_online_presence_to_friends(self):
        pres = self.bot.xmpp.make_presence(pfrom="18321445606@localhost",
                                           pto="friend.localhost",
                                           ptype="available")
        self.bot.user_online(pres)

        dut_p1 = self.bot.xmpp.send_queue.get_nowait()
        self.assertIsNotNone(dut_p1)
        self.assertIn('from="18321445606@localhost"', dut_p1)
        self.assertIn('to="18321445616@localhost"', dut_p1)

        with self.assertRaises(Empty):
            self.bot.xmpp.send_queue.get_nowait()

    def test_not_mobile_send_nothing(self):
        pres = self.bot.xmpp.make_presence(pfrom="admin@localhost",
                                           pto="friends.localhost",
                                           ptype="available")
        self.bot.user_online(pres)

        with self.assertRaises(Empty):
            self.bot.xmpp.send_queue.get_nowait()

    def test_not_register_mobile_send_nothing(self):
        pres = self.bot.xmpp.make_presence(pfrom="18321445696@localhost",
                                           pto="friends.localhost",
                                           ptype="available")
        self.bot.user_online(pres)

        with self.assertRaises(Empty):
            self.bot.xmpp.send_queue.get_nowait()

    def test_get_roster_send_result(self):
        rost = self.bot.xmpp.make_iq(ifrom="18321445606@localhost",
                                     ito="friends.localhost",
                                     itype="get")
        self.bot.xmpp.make_query_roster(rost)

        self.bot.get_roster(rost)

        dut_q1 = self.bot.xmpp.send_queue.get_nowait()
        self.assertIsNotNone(dut_q1)
        dut_e1 = ET.fromstring(dut_q1)
        self.assertEquals('18321445606@localhost', dut_e1.attrib['to'])
        self.assertEquals('friends.localhost', dut_e1.attrib['from'])
        self.assertEquals('result', dut_e1.attrib['type'])
        self.assertEquals(len(dut_e1[0].getchildren()), 3)
