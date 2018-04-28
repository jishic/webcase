#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# **********************************************************************
#
# Description: 云文本短信客户端模块
#
# Author: Peter Hu
#
# Created Date:2017/4/27
#
# Copyright (c) ShenZhen Montnets Technology,, Inc. All rights reserved.
#
# **********************************************************************
import time
import json
import traceback
import requests
import random
from . import smsmessage
# 文本短信发送客户端
class SmsClient():
    def __init__(self):
        self._userid = 'E102MX' #发送者帐号
        self._pwd = '3Rg1yH' #发送者帐号的密码
        self._url = 'http://api01.monyun.cn:7901/sms/v2/std/' #请前往您的控制台获取请求域名(IP)或联系梦网客服进行获取

    @property
    def userid(self):
        return self._userid

    @property
    def pwd(self):
        return self._pwd

    @property
    def url(self):
        return self._url

    #http post
    def postSmsMessage(self, message):
        fullurl = self.url + message.apiname
        try:
            r = None
            body = message.toJson()
            timeout = (5, 30)

            headers = {'Content-Type': 'application/json', 'Connection': 'Close'}
            # 短连接请求
            r = requests.post(fullurl, data=body, headers=headers, timeout=timeout)

            r.encoding = 'utf-8'
            debugStr = '\n[------------------------------------------------------------\n' + \
                       'http url:' + fullurl + '\n' + \
                       'headers:' + headers.__str__() + '\n' + \
                       body + '\n' + \
                       'status code:' + str(r.status_code) + '\n' + \
                       r.text + \
                       '\n-------------------------------------------------------------]\n'
            print (debugStr)

            # http请求失败
            if (r.status_code != requests.codes.ok):
                return message.makeupRet(SmsErrorCode.ERROR_310099)

            # 请求成功,解析服务器返回的json数据,
            rTest = json.loads(r.text)
            return rTest
        except SmsValueError as v:
            return message.makeupRet(v.errorcode)
        except requests.RequestException as e:
            print (traceback.format_exc().__str__())
            return message.makeupRet(SmsErrorCode.ERROR_310099)
        except Exception as e:
            print (traceback.format_exc().__str__())
            return message.makeupRet(SmsErrorCode.ERROR_310099)

    # 单条发送(短信)
    def singleSend(self ,telephone, verificationcode):
        message = smsmessage.SmsSingleMessage()
        #发送者帐号
        message.userid = self.userid
        #密码
        message.pwd = self.pwd
        #接收方手机号码
        message.mobile = telephone
        #验证码数字<=6位
        # randomnum = random.randint(100001,1000000)
        # print(randomnum)
        message.content = u'您登录系统的动态码为：' + verificationcode + '，动态码有效时间为60s，请注意保密。'
        #业务类型：最大可支持10个长度的ASCII字符串：字母，数字
        message.svrtype = '0123456789'
        #扩展号：长度不能超过6位，注意通道号+扩展号的总长度不能超过20位，若超出exno无效，如不需要扩展号则不用提交此字段或填空
        message.exno = '123456'
        #用户自定义流水编号：该条短信在您业务系统内的ID，比如订单号或者短信发送记录的流水号。填写后发送状态返回值内将包含这个ID。
        #最大可支持64位的ASCII字符串：字母、数字、下划线、减号，如不需要则不用提交此字段或填空
        message.custid = 'b3d0a2783d31b21b8573'
        #业务类型：最大可支持10个长度的ASCII字符串：字母，数字
        message.exdata = '0123456789'

        ret = self.postSmsMessage(message)
        print ('singleSend:', ret)
