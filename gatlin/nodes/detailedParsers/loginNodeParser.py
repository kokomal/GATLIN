# coding = utf-8

import gatlin.infra.commonUtils as util
import gatlin.infra.security as sec
import gatlin.preps.geo as geo
from gatlin.nodes.base import AbstractNodeParser
from gatlin.preps import params


# 专门的登录节点处理器
# context--{request, response, environ, initParam, session, misc}
# context包括6个成员:
# request和response代表每次的请求和返回，与请求密切相关，会随着工作流进行而变化
# environ代表环境变量，即在哪个环境下，flow的工作模式等
# initParam代表初始化参数，也可以认为是初始的入口参数
# session代表全局共享的业务上下文，会随着工作流进行而变化
# misc代表引擎的运行状态信息上下文，理论上不应该影响APP业务，只负责记录引擎运行信息
class LoginNodeParser(AbstractNodeParser):
    def prepare(self):
        reqParam = params.genericPackParam()
        util.inject_all(reqParam, self.context['initParam'])  # 取初始化参数
        ENV = self.context['environ']['env']
        sec.init(ENV)  # 初始化加密的公私钥
        self.pack_method(reqParam)
        biz = {}
        biz['loginType'] = "ORIGIN"
        biz['mobileNo'] = reqParam['mobileNo']  # 手机号
        biz['password'] = str(sec.encrypt(bytes(reqParam['password'], encoding='utf8')), 'utf-8')
        biz['geoInfo'] = str(geo.packGeo())  # 地理geo必传，否则会落库报latitude非空键异常
        reqParam["bizContent"] = str(biz)  # 业务数据
        self.context['request'] = reqParam  # 归根到底目的是为了拼装request参数

    # 重点在此处理session
    def fetch_resp(self):
        print('RESP OF CURRENT NODE', self.context['response'])
        token = self.context['response']['data']['token']  # token
        userNo = self.context['response']['data']['userNo']  # 获得userNo
        mobileNo = self.context['response']['data']['mobileNo']  # 获得userNo
        self.context['session']['token'] = token
        self.context['session']['userNo'] = userNo
        self.context['session']['mobileNo'] = mobileNo
        print('SESSION IS', self.context['session'])