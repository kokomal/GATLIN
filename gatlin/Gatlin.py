# coding=utf-8

import json
import unittest

import requests

import gatlin.infra.security as sec
from gatlin.preps import params, geo, consts

'''
Using PYTHON 3.7.3
Do not use for commercial purposes.
Copyright by Chenyuanjun
All rights reserved
'''


# [废弃]采用纯map方式拼接参数
def packJson():
    jsonstr = {"method": "qihoo.sdk.user.mobile.prequery", "bizContent": "{\"mobileNo\":\"+6308169999107\"}",
               "countryCode": "+63", "pageName": "index.html", "token": "", "userNo": "", "hostApp": "PHLLOAN",
               "version": "1.0.0", "timestamp": "1516171017941", "charset": "UTF-8", "sign": "", "custNo": "",
               "productCode": "PHLLOAN", "signType": "RSA", "appVersion": "1.0.0", "channelSource": "PHL_000",
               "sourceType": "APK", "networkType": "wifi",
               "deviceInfo": "{\"terminalType\":\"app\",\"deviceSn\":\"866049037447059\",\"deviceOs\":\"ANDROID\",\"deviceOsVersion\":\"7.0\",\"deviceIp\":\"10.93.146.175\",\"imsi\":\"460014055609890\",\"isRoot\":\"N\",\"isEmulator\":\"N\",\"networkType\":\"WIFI\",\"wifiMac\":\"B0:E5:ED:F6:39:58\",\"wifiName\":\"360jie\",\"brand\":\"HONOR\",\"model\":\"DUK-AL20\",\"usedStorage\":\"27459276800\",\"totalStorage\":\"56302223360\",\"factoryTime\":\"1501216717000\",\"deviceName\":\"DUK-AL20\",\"deviceFingerPrintM2\":\"d294f2bbe2e9d10a30b8e7f82b709dde\",\"deviceFingerPrintM2N\":\"fe2a143c58104253eaa3ffd6d7a6c980\",\"deviceFingerPrintTd\":\"eyJvcyI6ImFuZHJvaWQiLCJ2ZXJzaW9uIjoiMy4wLjMiLCJwYWNrYWdlcyI6ImNvbS5qaW5zaGFuZy5wZGwuYW5kcm9pZF8xLjAuMCIsInByb2ZpbGVfdGltZSI6MTM4LCJ0b2tlbl9pZCI6Ikh2aFAzSDlqVDlSRFVSajl6RkVvT3ZTME1LcldhZ0hcL2VsVEh5cFc2NTdjbEFjMDdKWFRLb3JTc3Blemk4NG12d00wQjVKWXdiQW9kZVAxSGFxTmVkQT09In0=\",\"deviceFingerPrintBr\":\"\",\"uuid\":\"00000000-7e58-1d92-ffff-ffffe1669361\",\"buildSerial\":\"6EB0217823000929\",\"bssid\":\"94:28:2e:8f:b9:a0\",\"isYUNOS\":\"N\",\"regId\":\"\",\"androidId\":\"1562e7419dafb885\"}",
               "wifiMac": "B0:E5:ED:F6:39:58", "subChannel": "", "h5Version": "1010199999"}
    print('*' * 10, jsonstr, '*' * 10)
    return jsonstr


# 通用post请求封装
def myJsonPost(urlStr, param):
    return requests.post(url=urlStr, json=param, headers={'Content-Type': 'application/json'})


# 自定义的参数packer，可以在已有的param上自定义任意KV，下同
def packPreQueryParam():
    param = params.genericPackParam()
    param["method"] = consts.PREQUERY
    param["userNo"] = "UR6829095035230650368"
    biz = {}
    biz["mobileNo"] = "+6308169999107"
    param["bizContent"] = str(biz)  # 业务数据
    printParam(param)
    return param


def packMcMsgCountNewParam():
    param = params.genericPackParam()
    param["method"] = consts.MCMSG_COUNTNEW
    param["userNo"] = "UR6829095035230650368"
    param["bizContent"] = "{}"  # 业务数据
    printParam(param)
    return param


def packMcMsgQueryParam():
    param = params.genericPackParam()
    param["method"] = consts.MCMSG_QUERY
    param['userNo'] = 'UR6829095035230650368'
    biz = {}
    biz["msgCurrentSize"] = "0"
    biz["pageSize"] = "20"
    param["bizContent"] = str(biz)  # 业务数据
    printParam(param)
    return param


def packSmsSendParam():
    param = params.genericPackParam()
    param["method"] = consts.SMS_SEND
    param['userNo'] = 'UR6740732993587994624'
    biz = {}
    biz["templateName"] = "lps_verify_code"
    biz["smscodeFlag"] = "Y"
    biz["mobileNo"] = "+6308169999611"
    param["bizContent"] = str(biz)  # 业务数据
    printParam(param)
    return param


def packApplSummaryQueryParam():
    param = params.genericPackParam()
    param["method"] = consts.APPL_SUMMARY_QUERY
    param['userNo'] = 'UR6851459076372574208'
    biz = {}
    param["bizContent"] = str(biz)  # 业务数据
    # printParam(param)
    return param


# 注册用户
def packRegisterParam():
    param = params.genericPackParam()
    param["method"] = consts.REGISTER
    biz = {}
    biz['mobileNo'] = '+6308132000100'  # 手机号
    biz['password'] = str(sec.encrypt(b'123456'), 'utf-8')
    biz['geoInfo'] = str(geo.packGeo())  # 地理geo必传，否则会落库报latitude非空键异常
    param["bizContent"] = str(biz)  # 业务数据
    printParam(param)
    return param


# 用户登录
def packLoginParam():
    param = params.genericPackParam()
    param["method"] = consts.LOGIN
    biz = {}
    biz['loginType'] = "ORIGIN"
    biz['mobileNo'] = '+6308132000100'  # 手机号
    biz['password'] = str(sec.encrypt(b'123456'), 'utf-8')
    biz['geoInfo'] = str(geo.packGeo())  # 地理geo必传，否则会落库报latitude非空键异常
    param["bizContent"] = str(biz)  # 业务数据
    # printParam(param)
    return param


def get_pretty_print(json_object):
    return json.dumps(json_object, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)


def printParam(param):
    print('>' * 8, 'PARAM', '>' * 8, "\n", get_pretty_print(param))


def printReturn(ret):
    print('<' * 8, 'RESULT', '<' * 8, "\n", get_pretty_print(ret))


class gatlin(unittest.TestCase):

    def tearDown(self):
        # 每个测试用例执行之后做操作
        printReturn(self.ret)
        print('=' * 150)

    def setUp(self):
        # 每个测试用例执行之前做操作
        print('=' * 150)

    @classmethod
    def tearDownClass(self):
        print('FINISHED...')

    @classmethod
    def setUpClass(self):
        print('STARTING...')
        self.ENV = "DEV"  # ~~~~~~~~~~~~~~~~~~~~~~这里改环境!!!~~~~~~~~~~~~~~~~~~~~~~
        sec.init(self.ENV)  # 初始化加密的公私钥，将来可以把token也塞入类的成员变量
        self.context = {}  # 初始化上下文

    def test_1_preQuery(self):
        # -------------------------登录前预校验------------------------------
        urlStr = consts.getEnviron(self.ENV) + consts.PREQUERY
        res = myJsonPost(urlStr, packPreQueryParam())
        self.ret = res.text

    def test_2_mcMsgCount(self):
        # -------------------------消息中心消息数-----------------------------
        urlStr = consts.getEnviron(self.ENV) + consts.MCMSG_COUNTNEW
        res = myJsonPost(urlStr, packMcMsgCountNewParam())
        self.ret = res.text

    def test_3_mcMsgQuery(self):
        # -------------------------消息中心列表查询---------------------------
        urlStr = consts.getEnviron(self.ENV) + consts.MCMSG_QUERY
        res = myJsonPost(urlStr, packMcMsgQueryParam())
        self.ret = res.text

    def test_4_webSendSms(self):
        # -------------------------WEB发送验证码----------------------------
        urlStr = consts.getEnviron(self.ENV) + consts.MCMSG_QUERY
        res = myJsonPost(urlStr, packSmsSendParam())
        self.ret = res.text

    def test_5_applSummaryQuery(self):
        # -------------------------首页信息查询------------------------------
        urlStr = consts.getEnviron(self.ENV) + consts.APPL_SUMMARY_QUERY
        res = myJsonPost(urlStr, packApplSummaryQueryParam())
        self.ret = res.text

    def test_6_registerOnly(self):
        # -------------------------手机号注册，返回token------------------------------
        urlStr = consts.getEnviron(self.ENV) + consts.REGISTER
        res = myJsonPost(urlStr, packRegisterParam())
        self.ret = res.text
        retJson = json.loads(self.ret)
        token = retJson['data']['token']
        print("Fetch Register Token", token)

    def test_7_loginOnly(self):
        # -------------------------手机号登录，返回token------------------------------
        urlStr = consts.getEnviron(self.ENV) + consts.LOGIN
        res = myJsonPost(urlStr, packLoginParam())
        self.ret = res.text
        retJson = json.loads(self.ret)
        token = retJson['data']['token']
        self.context['token'] = token  # token放入上下文
        print("Fetch LOGIN Token", token)

    def test_8_oneDragon(self):
        # -------------------------一条龙------------------------------
        urlStr = consts.getEnviron(self.ENV) + consts.LOGIN
        res = myJsonPost(urlStr, packLoginParam())
        self.ret = res.text
        printReturn(self.ret)
        retJson = json.loads(self.ret)
        token = retJson['data']['token']  # 更新token
        userNo = retJson['data']['userNo']  # 获得userNo
        self.context['token'] = token  # 放入上下文
        self.context['userNo'] = userNo
        # -------------------------首页信息查询(带token和userNo)------------------------------
        urlStr = consts.getEnviron(self.ENV) + consts.APPL_SUMMARY_QUERY
        param = packApplSummaryQueryParam()
        param['userNo'] = self.context['userNo']  # 取上下文的token，下同
        param['token'] = self.context['token']
        res = myJsonPost(urlStr, param)
        self.ret = res.text


if __name__ == "__main__":
    unittest.main()
