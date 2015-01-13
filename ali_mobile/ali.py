#!/usr/bin/env python
# encoding: utf-8

import M2Crypto
import urllib
import requests
import base64
from alias import config


def make_info(trade_no, subject, body, total_fee, notify_url):
    info_data = {
        'service': config.SERVICE,
        'partner': config.PARTNER,
        'seller_id': config.SELLER_ID,
        '_input_charset': config.INPUT_CHARSET,
        'out_trade_no': trade_no,
        'subject': subject,
        'payment_type': config.PAYMENT_TYPE,
        'body': body,
        'total_fee': total_fee,
        'notify_url': urllib.quote(notify_url),
    }

    ks = info_data.keys()
    ks.sort()

    sorted_info_data = [(k, info_data[k]) for k in ks]
    sorted_str_data = ['%s="%s"' % (k, v) for k, v in sorted_info_data]

    unsign_info_str = '&'.join(sorted_str_data)

    private_key = M2Crypto.RSA.load_key(config.OUR_PRIVATE_KEY_FILE)
    m = M2Crypto.EVP.MessageDigest('sha1')
    if isinstance(unsign_info_str, unicode):
        m.update(unsign_info_str.encode('utf-8'))
    else:
        m.update(unsign_info_str)
    digest = m.final()

    sign = private_key.sign(digest, 'sha1')
    sign = base64.encodestring(sign)
    sign_type = 'RSA'

    sign = urllib.quote(sign)
    info_str = '&'.join([unsign_info_str, 'sign="%s"' % sign,
                         'sign_type="%s"' % sign_type])

    return info_str


def verify_callback(post_data):
    u"""
    验证回调请求.
    签名和请求来源
    """
    verify_status = verify_notify(post_data)
    if not verify_status:
        return False
    # 验证是否是来自支付宝的请求
    notify_status = verify_source(post_data)
    if not notify_status:
        return False
    return True


def verify_notify(post_data):
    u"""
    验证支付宝毁掉签名
    """
    post = dict(post_data)
    sign = ''.join(post.pop('sign'))
    # sign = sign[1:-1]
    sign = urllib.unquote(sign)
    post.pop('sign_type')
    ks = post.keys()
    ks.sort()
    sorted_sign_data = ['%s=%s' % (k, post_data.get(k)) for k in ks]
    sign_str = '&'.join(sorted_sign_data)
    if isinstance(sign_str, unicode):
        sign_str = sign_str.encode('utf-8')

    public_key = M2Crypto.RSA.load_pub_key(config.ALI_PUBLIC_KEY_FILE)
    m = M2Crypto.EVP.MessageDigest('sha1')
    m.update(sign_str)
    digest = m.final()

    sign_result = public_key.verify(digest, base64.decodestring(sign), 'sha1')

    return sign_result


def verify_source(post_data):
    u"""
    验证请求是否来自支付宝
    """
    partner = post_data.get('partner')
    if not partner:
        partner = post_data.get('seller_id')
    notify_id = post_data.get('notify_id')

    method = config.VERIFY_METHOD
    if method == 'https':
        verify_url = config.HTTPS_VERIFY_URL
        params = config.HTTPS_PARAM
    else:
        verify_url = config.HTTP_VERIFY_URL
        params = config.HTTP_PARAM

    update = {
        'partner': partner,
        'notify_id': notify_id,
    }
    params.update(update)
    response = requests.get(verify_url, params=params)
    if response.text in ['true', u'true']:
        return True
    return False
