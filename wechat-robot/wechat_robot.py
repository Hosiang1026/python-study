#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itchat
from tuling import get_response
from itchat.content import *

itchat.auto_login(hotReload=True)

@itchat.msg_register(TEXT)
def text_reply(msg):
    print(msg)
    if msg['FromUserName'] == '@efd311ea496fbfcd5b55ae8a164512845605463d6c5703cab311c0f8b4018f3a':
        return '你是？'
    elif msg['Text'] == '狂欢马克思':
        return '没错，我就是狂欢马克思！哈哈哈~'
    else:
        return get_response(msg['Text'])

@itchat.msg_register(TEXT, isGroupChat = True)
def text_reply(msg):
    print(msg)
    white_list = {
        '张喜庄92号院':'@@427f7ba31d25e1dc70f88978bfbc861a6142573141a0fbcddb1a4b11af16e4c5',
        }
    if msg['FromUserName'] in white_list.values():
        return get_response(msg['Text'])

itchat.run(debug=True)