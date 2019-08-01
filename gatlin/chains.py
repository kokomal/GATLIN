# coding=utf-8
from gatlin.preps import geo,consts,params

import unittest
import json
import gatlin.infra.security as security
import gatlin.Gatlin as Gatlin


'''
Using PYTHON 3.7.3
Do not use for commercial purposes.
Copyright by Chenyuanjun
All rights reserved
'''

# 用户登录
def packLoginParam(mobile, bytePwd):
    paramIn = params.genericPackParam()
    paramIn["method"] = consts.LOGIN
    biz = {}
    biz['loginType'] = "ORIGIN"
    biz['mobileNo'] = mobile  # 手机号
    biz['password'] = str(security.encrypt(bytePwd), 'utf-8')
    biz['geoInfo'] = str(geo.packGeo())  # 地理geo必传，否则会落库报latitude非空键异常
    paramIn["bizContent"] = str(biz)  # 业务数据
    Gatlin.printParam(paramIn)
    return paramIn

# 还款记录
def packRefundRecordQueryParam():
    paramIn = params.genericPackParam()
    paramIn["method"] = consts.REFUND_RECORD_QUERY
    biz = {}
    biz['contractNo'] = '6851471332867129344'
    biz['custNo'] = 'CT6851459341117042688'
    biz['loanNo'] = '6857427969591234560'
    biz['mobileNo'] = '+6308132000071'
    paramIn["bizContent"] = str(biz)  # 业务数据
    Gatlin.printParam(paramIn)
    return paramIn

def packSupplementlistQWueryParam():
    paramIn = params.genericPackParam()
    paramIn["method"] = consts.SUPPLEMENT_LIST_QUERY
    biz = {}
    biz['mobileNo'] = '+6308062400111'
    biz['custNo'] = 'CT6829156253144350720'
    biz['loanNo'] = '6829491650026262528'
    biz['contractNo'] = '6829233129166528512'
    paramIn["bizContent"] = str(biz)  # 业务数据
    Gatlin.printParam(paramIn)
    return paramIn

# 从登录开始一条龙
class loginchains(unittest.TestCase):
    def tearDown(self):
        # 每个测试用例执行之后做操作
        Gatlin.printReturn(self.ret)
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
        self.ENV = "PH_DEV"  # ~~~~~~~~~~~~~~~~~~~~~~这里改环境!!!~~~~~~~~~~~~~~~~~~~~~~
        security.init(self.ENV)  # 初始化加密的公私钥
        self.context = {} # 初始化上下文
        loginPrepare = packLoginParam('+6308062400111', b'123456') # ~~~~~~~~~~~~~~~~~~~~~~这里改用户!!!~~~~~~~~~~~~~~~~~~~~~~
        urlStr = consts.getEnviron(self.ENV) + consts.LOGIN
        res = Gatlin.myJsonPost(urlStr, loginPrepare)
        retJson = json.loads(res.text)
        Gatlin.get_pretty_print(retJson)
        token = retJson['data']['token']
        userNo = retJson['data']['userNo']  # 获得userNo
        mobileNo = retJson['data']['mobileNo']  # 获得mobileNo
        custNo = retJson['data']['custNo']  # 获得mobileNo
        print("Fetch LOGIN Token", token)
        self.context['token'] = token # token放入上下文
        self.context['userNo'] = userNo # userNo放入上下文
        self.context['mobileNo'] = mobileNo # userNo放入上下文
        self.context['custNo'] = custNo # userNo放入上下文
        
    # 威力加强版一条龙
    def test_1_oneDragon(self):
        #-------------------------首页信息查询(带token和userNo)------------------------------
        urlStr = consts.getEnviron(self.ENV) + consts.APPL_SUMMARY_QUERY
        paramIn = Gatlin.packApplSummaryQueryParam()
        paramIn['userNo'] = self.context['userNo'] # 取上下文的userNo，下同
        paramIn['token'] = self.context['token']
        Gatlin.printParam(json.dumps(paramIn))
        self.ret = json.loads(Gatlin.myJsonPost(urlStr, paramIn).text)
        
    def test_2_oneDragon(self):
        #-------------------------首页信息查询(带token和userNo)------------------------------
        urlStr = consts.getEnviron(self.ENV) + consts.REFUND_RECORD_QUERY
        paramIn = packRefundRecordQueryParam()
        paramIn['userNo'] = self.context['userNo'] # 取上下文的userNo，下同
        paramIn['token'] = self.context['token']
        Gatlin.printParam(paramIn)
        self.ret = json.loads(Gatlin.myJsonPost(urlStr, paramIn).text)
        
    def test_3_oneDragon(self):
        #-------------------------补件信息查询(带token和userNo)------------------------------
        urlStr = consts.getEnviron(self.ENV) + consts.SUPPLEMENT_LIST_QUERY
        paramIn = packSupplementlistQWueryParam()
        paramIn['userNo'] = self.context['userNo'] # 取上下文的userNo，下同
        paramIn['token'] = self.context['token']
        paramIn['custNo'] = self.context['custNo']
        Gatlin.printParam(paramIn)
        self.ret = json.loads(Gatlin.myJsonPost(urlStr, paramIn).text)