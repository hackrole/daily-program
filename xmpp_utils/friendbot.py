#!/usr/bin/env python
# encoding: utf-8

import sys
import logging
import signal
from mongoengine import connect
from sleekxmpp import ComponentXMPP
from sleekxmpp import Callback, StanzaPath, MatchXPath
from tornado.options import options, define, parse_command_line
from sleekxmpp.stanza.roster import RosterItem


logging.basicConfig(
    level=logging.DEBUG,
    stream=sys.stdout,
)


class FriendBot(object):
    u"""
    好友功能bot,负责管理好友的上线下线通知,添加好友黑名单等功能
    """

    def __init__(self, jid, pwd, host, port, mongo_host, mongo_db):
        self.jid = jid
        self.pwd = pwd
        self.host = host
        self.port = port
        self.mongo_host = mongo_host
        self.mongo_db = mongo_db

        self.xmpp = ComponentXMPP(jid, pwd, host, port)

        self.xmpp.register_plugin("xep_0004")
        self.xmpp.register_plugin("xep_0030")
        self.xmpp.register_plugin("xep_0045")
        self.xmpp.register_plugin("xep_0198")
        self.xmpp.register_plugin("xep_0199")

        self.xmpp.add_event_handler("session_start", self.session_start)

        self.xmpp.register_handler(
            Callback('friend online', StanzaPath("presence@type=available"),
                     self.user_online))
        self.xmpp.register_handler(
            Callback('friend offline', StanzaPath("presence@type=unavailable"),
                     self.user_offline))
        self.xmpp.register_handler(
            Callback('ask friend', StanzaPath("presence@type=subscript"),
                     self.ask_friend))
        self.xmpp.register_handler(
            Callback('ack friends', StanzaPath("presence@type=subscripted"),
                     self.ack_friend))
        self.xmpp.register_handler(
            Callback('unack friend', StanzaPath("presence@type=unsubscript"),
                     self.unack_friend))
        # TODO black

        roster_stanza = MatchXPath("{%s}iq/{%s}query" % (self.xmpp.default_ns,
                                                         "jabber:iq:roster"))
        self.xmpp.register_handler(Callback("get roster", roster_stanza,
                                            self.get_roster))

        # signal ctrl-c to exit
        signal.signal(signal.SIGINT, self.exit_handle)

        # connect mongodb
        connect(self.mongo_db, host=self.mongo_host)

    def ask_friend(self, presence):
        pass

    def ack_friend(self, presence):
        pass

    def unack_friend(self, presence):
        pass

    def exit_handle(self, signal, frame):
        logging.info("you press Ctrl-c, now the xmpp will exit.")
        try:
            self.xmpp.disconnect(wait=True)
        except Exception as e:
            logging.warning(e.message)
        finally:
            logging.info("=>>> now exit and close.")
            sys.exit(-1)

    def get_roster(self, iq):
        print "hello world"
        user_jid = iq['from']

        result = self.xmpp.make_iq_result(ifrom="friends.localhost",
                                          ito=user_jid)
        self.xmpp.make_query_roster(result)

        a = RosterItem()
        a.values = {"jid": "rel_jid", "name": "rel_name",
                    "subscription": "rel_sub"}
        result['roster'].append(a)

        result.send()

    def user_online(self, presence):
        user_jid = presence['from']

        self.xmpp.send_presence(pfrom=user_jid, pto="new_jid",
                                ptype="available")

    def user_offline(self, presence):
        user_jid = presence['from']

        self.xmpp.send_presence(pfrom=user_jid, pto="new_jid",
                                ptype="unavailable")

    def start(self):
        u"""
        启动好友bot
        """
        if self.xmpp.connect(use_tls=False):
            self.xmpp.process(block=True)
        else:
            logging.warning("connect xmpp server error")
            raise Exception("connect failes")

    def session_start(self, event):
        self.xmpp.send_presence()


if __name__ == "__main__":
    define("mongo_host", default="127.0.0.1", help="mongo host to connect")
    define("mongo_db", default="nchat_dev", help="mongo db to use")
    define("jid", default="friends.localhost", help="component jid")
    define("pwd", default="joygin123", help="component secrect")
    define("host", default="127.0.0.1", help="xmpp host to connect")
    define('port', default='9289', help="component port to connect")

    parse_command_line()

    jid = options.jid
    pwd = options.pwd
    host = options.host
    port = options.port
    mongo_host = options.mongo_host
    mongo_db = options.mongo_db

    friendBot = FriendBot(jid, pwd, host, port, mongo_host, mongo_db)
    logging.info("start login bot now")
    friendBot.start()
