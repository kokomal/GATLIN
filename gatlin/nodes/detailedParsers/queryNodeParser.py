# coding = utf-8

import gatlin.infra.commonUtils as util
import gatlin.infra.security as sec
import gatlin.preps.geo as geo
from gatlin.nodes.base import AbstractNodeParser
from gatlin.preps import params
import json


class SummaryQueryNodeParser(AbstractNodeParser):
    def prepare(self):
        public_req_param = params.genericPackParam()
        util.inject_all_soft(public_req_param, self.context['session'])  # 取初始化参数
        self.pack_method(public_req_param)
        biz = {}
        public_req_param['userNo'] = self.context['session']['userNo']
        public_req_param["bizContent"] = str(biz)  # 业务数据
        public_req_param["deviceInfo"] = str(self.context['session']['deviceInfo'])
        self.context['request'] = public_req_param  # 归根到底目的是为了拼装request参数
        print("summQ", public_req_param)

    # 重点在此处理session
    def fetch_resp(self):
        print('RESP OF CURRENT NODE', json.dumps(self.context['response']))
