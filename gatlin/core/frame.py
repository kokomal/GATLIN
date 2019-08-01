# coding=utf-8
from gatlin.preps import geo,consts, params

import gatlin.infra.security as security
import json
import gatlin.Gatlin as Gatlin

# 用户登录
def packLoginParam(paramIn):
    paramOut = params.genericPackParam()
    paramOut["method"] = consts.LOGIN
    biz = {}
    biz['loginType'] = "ORIGIN"
    biz['mobileNo'] = paramIn['mobileNo']   # 手机号
    pwd = paramIn['password']
    biz['password'] = str(security.encrypt(bytes(pwd, encoding ="utf8")), 'utf-8')
    biz['geoInfo'] = str(geo.packGeo())  # 地理geo必传，否则会落库报latitude非空键异常
    paramOut["bizContent"] = str(biz)  # 业务数据
    return paramOut


# 注册用户
def packRegisterParam(paramIn):
    paramOut = params.genericPackParam()
    paramOut["method"] = consts.REGISTER
    biz = {}
    biz['mobileNo'] = paramIn['mobileNo']  # 手机号
    pwd = paramIn['password']
    biz['password'] = str(security.encrypt(bytes(pwd, encoding ="utf8")), 'utf-8')
    biz['geoInfo'] = str(geo.packGeo())  # 地理geo必传，否则会落库报latitude非空键异常
    paramOut["bizContent"] = str(biz)  # 业务数据
    return paramOut


# 还款记录
def packRefundRecordQueryParam(paramIn):
    paramOut = params.genericPackParam()
    paramOut["method"] = consts.REFUND_RECORD_QUERY
    biz = {}
    biz['contractNo'] = paramIn['contractNo']
    biz['custNo'] = paramIn['custNo']
    biz['loanNo'] = paramIn['loanNo']
    biz['mobileNo'] = paramIn['mobileNo']
    paramOut["bizContent"] = str(biz)  # 业务数据
    Gatlin.printParam(paramOut)
    return paramOut


# 更加高级的集成测试框架
class MainFrame:

    # 指定启动的初始化方法，和参数
    @classmethod
    def __init__(self, initMethod, paramIn):
        self.curMethod = initMethod
        self.paramIn = paramIn
        self.nextMethod = None
        self.context = {}
        getattr(self, self.curMethod)(self)

    def clear(self):
        self.curMethod = None
        self.nextMethod = None
        self.context = {}

    # 强制指定顺序
    def mandatoryWalk(self, orderMethods):
        print("---MANDATORY BEGINS---")
        for orderMethod in orderMethods:
            getattr(self, orderMethod)()
            Gatlin.printReturn(json.loads(self.ret))
        print("---MANDATORY ENDS---")
        
    # 给定初始值，环环相扣
    def stickyWalk(self):
        print("---HERE WE GO!---")
        if not self.curMethod:
            return
        while 1:
            getattr(self, self.curMethod)()
            Gatlin.printReturn(json.loads(self.ret))
            if self.nextMethod:
                self.curMethod = self.nextMethod
            else:
                print("---HERE WE STOP!---")
                break


# 从用户登录开始的一系列动作        
class LoginTester(MainFrame):

    def myInit(self):
        print('STARTING...')
        self.ENV = self.paramIn['environ']
        security.init(self.ENV)  # 初始化加密的公私钥
        self.context = {}  # 初始化上下文
        loginPrepare = packLoginParam(self.paramIn)
        urlStr = consts.getEnviron(self.ENV) + consts.LOGIN
        res = Gatlin.myJsonPost(urlStr, loginPrepare)
        retJson = json.loads(res.text)
        token = retJson['data']['token']
        userNo = retJson['data']['userNo']  # 获得userNo
        print("Fetch LOGIN Token", token)
        self.context['token'] = token  # token放入上下文
        self.context['userNo'] = userNo  # userNo放入上下文
        self.curMethod = "biz1"
    
    def biz1(self):
        print("BIZ1!!")
        self.nextMethod = "biz2"
        
    def biz2(self):
        print("BIZ2!!")
        self.nextMethod = "biz3"
        
    def biz3(self):
        print("BIZ3!!")
        self.nextMethod = None
        
    def refundRecordQuery(self):
        refundPrepare = packRefundRecordQueryParam(self.paramIn)
        urlStr = consts.getEnviron(self.ENV) + consts.REFUND_RECORD_QUERY
        self.ret = Gatlin.myJsonPost(urlStr, refundPrepare).text



# 从用户注册开始的一系列动作        
class RegisterTester(MainFrame):

    def myInit(self):
        print('STARTING...')
        self.ENV = self.paramIn['env']
        security.init(self.ENV)  # 初始化加密的公私钥
        self.context = {}  # 初始化上下文
        regPrepare = packRegisterParam(self.paramIn)
        print(regPrepare)
        urlStr = consts.getEnviron(self.ENV) + consts.REGISTER
        res = Gatlin.myJsonPost(urlStr, regPrepare)
        retJson = json.loads(res.text)
        print(retJson)
        token = retJson['data']['token']
        userNo = retJson['data']['userNo']  # 获得userNo
        print("Fetch REGISTER Token", token)
        self.context['token'] = token  # token放入上下文
        self.context['userNo'] = userNo  # userNo放入上下文
        self.curMethod = "biz4"
    
    def biz4(self):
        print("BIZ4!!")
        self.nextMethod = "biz5"
        
    def biz5(self):
        print("BIZ5!!")
        self.nextMethod = "biz6"
        
    def biz6(self):
        print("BIZ6!!")
        self.nextMethod = None

       
if __name__ == '__main__':
    paramIn = {}  # 入参包括环境、手机号和密码等账户信息
    paramIn['env'] = 'PH_DEV'
    paramIn['mobileNo'] = '+6308132000071'
    paramIn['password'] = b'123456'
    # 以下是业务参数
    paramIn['contractNo'] = '6851471332867129344'
    paramIn['custNo'] = 'CT6851459341117042688'
    paramIn['loanNo'] = '6857427969591234560'
    
    logi = LoginTester("myInit", paramIn)  # 给定一个初始方法，一路走下去
#     logi.stickyWalk()
    logi.mandatoryWalk(["refundRecordQuery"])  # 强制指定顺序走下去,无视nextMethod
#---------------------------------------------------------------------------
#     print('-' * 80)
#     paramIn = {}  # 入参包括环境、手机号和密码等账户信息
#     paramIn['environ'] = 'DEV'
#     paramIn['mobile'] = '+6308132000110'
#     paramIn['password'] = b'123456'
#     reg = RegisterTester("myInit", paramIn)  # 给定一个初始方法，一路走下去
#     reg.stickyWalk()
#     reg.mandatoryWalk(["biz5", "biz6"])  # 强制指定顺序走下去,无视nextMethod
