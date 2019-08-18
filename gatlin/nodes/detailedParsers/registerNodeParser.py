# coding = utf-8
import gatlin.infra.commonUtils as util
import gatlin.infra.security as sec
from gatlin.nodes.base import AbstractNodeParser
from gatlin.preps import params


class RegisterNodeParser(AbstractNodeParser):
    def prepare(self):
        public_req_param = params.genericPackParam()
        util.inject_all_soft(public_req_param, self.context['session'])  # 取初始化参数
        ENV = self.context['environ']['env']
        sec.init(ENV)  # 初始化加密的公私钥
        self.pack_method(public_req_param)
        biz = {}
        biz['loginType'] = "ORIGIN"
        biz['mobileNo'] = self.context['environ']['mobileNo']  # 手机号和password放到了environ里面
        biz['password'] = str(sec.encrypt(bytes(self.context['environ']['password'], encoding='utf8')), 'utf-8')
        biz['geoInfo'] = str(self.context['session']['geo'])  # 地理geo必传，否则会落库报latitude非空键异常
        public_req_param["bizContent"] = str(biz)  # 业务数据
        public_req_param["deviceInfo"] = str(self.context['session']['deviceInfo'])
        self.context['request'] = public_req_param  # 归根到底目的是为了拼装request参数
        print("REG PARAM", public_req_param)

    # 重点在此处理session
    def fetch_resp(self):
        print('RESP OF CURRENT NODE', self.context['response'])
        if 'data' in self.context['response']:
            token = self.context['response']['data']['token']  # token
            userNo = self.context['response']['data']['userNo']  # 获得userNo
            mobileNo = self.context['response']['data']['mobileNo']  # 获得userNo
            self.context['session']['token'] = token
            self.context['session']['userNo'] = userNo
            self.context['session']['mobileNo'] = mobileNo
            print('SESSION IS', self.context['session'])
