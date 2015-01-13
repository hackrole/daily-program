#!/usr/bin/env python
# encoding: utf-8

import os
import re
import sys
import logging
import signal
from sleekxmpp import JID
from sleekxmpp import ClientXMPP
from mongoengine import connect
from tornado.options import options, define, parse_command_line


fp = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'logs/login_bot.log'
)
logging_format = "%(asctime)s [%(levelname)s] %(message)s"
logging.basicConfig(
    level=logging.DEBUG,
    stream=sys.stdout,
    #filename=fp,
    format=logging_format
)


class LoginBot(object):

    def __init__(self, jid, pwd, mmongo_host, mong_db):
        self.jid = jid
        self.xmpp = ClientXMPP(jid, pwd)
        self.ehost = '127.0.0.1'
        self.eport = '5222'

        # data form
        self.xmpp.register_plugin('xep_0004')
        # service disvovery
        self.xmpp.register_plugin('xep_0030')
        # session manager
        self.xmpp.register_plugin('xep_0198')
        # ping
        self.xmpp.register_plugin('xep_0199')

        self.xmpp.add_event_handler('session_start', self.session_start)
        self.xmpp.add_event_handler("message", self.message)

        # ping schedule
        #self.xmpp.schedule('login ping', 120, self.login_ping)

        self.mobile_re = re.compile('\d{11}')
        self.token_re = re.compile('[-0-9a-z\ ]{0,100}')

        # signal ctrl-c to exit
        signal.signal(signal.SIGINT, self.exit_handle)

        # connect mongo
        connect(mdb, host=mhost)

    def exit_handle(self, signal, frame):
        logging.info("you press Ctrl-c, now the xmpp will exit.")
        self.xmpp.disconnect(wait=True)
        logging.info("=>>> now exit and close.")
        sys.exit(-1)

    def start(self):
        u"""
        启动xmpp聊天机器人
        """
        if self.xmpp.connect((self.ehost, self.eport), use_tls=False):
            self.xmpp.process(block=True)
        else:
            raise Exception('connect fail')

    def session_start(self, event):
        self.xmpp.send_presence()
        #self.client.get_roster()

    def login_ping(self):
        pass

    def message(self, msg):
        u"login/logout/get_token处理"
        mtype = msg['type']
        fjid = msg['from']
        subject = msg['subject']
        body = msg['body']

        if mtype != 'chat':
            return

        mobile = JID(fjid).username
        if self.mobile_re.match(mobile) is None:
            return

        if body is not None and self.token_re.match(body) is None:
            body = None

        if subject == 'login':
            return self.login(fjid, body)
        elif subject == 'logout':
            return self.logout(fjid)
        elif subject == 'get_token':
            return self.get_token(fjid, body)

    def login(self, fjid, body):
        pass

    def logout(self, fjid):
        pass

    def get_token(self, fjid, body):
        pass


if __name__ == "__main__":
    define('mongo_host', default='127.0.0.1', help='mongo host to connect')
    define('mongo_db', default='nchat_dev', help='mongo db to use')
    define('login_jid', default='login@localhost/bot',
           help='login bot jid')
    define('login_pwd', default='joygin123', help='login bot password')

    parse_command_line()
    jid = options.login_jid
    pwd = options.login_pwd
    mhost = options.mongo_host
    mdb = options.mongo_db

    bot = LoginBot(jid, pwd, mhost, mdb)
    logging.info("start login bot now")
    bot.start()
