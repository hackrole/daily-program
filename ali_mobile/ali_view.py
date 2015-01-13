#!/usr/bin/env python
# encoding: utf-8

u"""
使用支付宝请求和回调
"""

import logging
import utils
from django.http import HttpResponse


def get_pay_info(request):
    msg = str(request)
    log = logging.getLogger('ali_pay')
    log.info(msg)

    trade_no = "trade_no"
    subject = "subject"
    body = "body"
    total_fee = 1
    notify_url = "callback_url"

    info_str = utils.make_info(trade_no, subject, body, total_fee, notify_url)

    return HttpResponse(info_str)


def order_callback(request):
    u"""
    普通订单支付回调
    设置订单支付状态,同时将金额添加到用户的冻结余额中
    """
    msg = str(request)
    log = logging.getLogger('ali_callback')
    log.info(msg)

    if request.method != 'POST':
        return HttpResponse('fail')

    # 验证请求来自支付宝, 测试时应该过滤掉
    post_data = request.POST
    verify_result = utils.verify_callback(post_data)
    if not verify_result:
        return HttpResponse('fail')

    trade_no = request.POST.get('out_trade_no')
    trade_status = request.POST.get('trade_status')
    total_fee = float(request.POST.get('total_fee'))
    print trade_no, total_fee

    if trade_status in ["TRADE_FINISHED", "TRADE_SUCCESS"]:
        # XXX done yourthings here

        return HttpResponse('success')

    if trade_status in ['WAIT_BUYER_PAY']:
        # XXX done yourthings here

        return HttpResponse('success')

    return HttpResponse('fail')
