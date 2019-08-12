# coding = utf-8

import json

import gatlin.infra.commonUtils as util
from gatlin.nodes.base import AbstractNodeParser
from gatlin.preps import params


class ItemCommitNodeParser(AbstractNodeParser):
    def prepare(self):
        public_req_param = params.genericPackParam()
        util.inject_all_soft(public_req_param, self.context['session'])  # 取初始化参数
        self.pack_method(public_req_param)
        biz = {}
        public_req_param['userNo'] = self.context['session']['userNo']
        public_req_param['token'] = self.context['session']['token']
        public_req_param["bizContent"] = str(biz)  # 业务数据
        public_req_param["deviceInfo"] = str(self.context['session']['deviceInfo'])
        self.context['request'] = public_req_param  # 归根到底目的是为了拼装request参数
        print('ItemCommitQ', public_req_param)

    # 重点在此处理session
    def fetch_resp(self):
        print('RESP OF CURRENT NODE', json.dumps(self.context['response']))
        node_code = self.context['response']['data']['nodeCode']  # node_code
        node_no = self.context['response']['data']['nodeNo']  # node_no
        flow_no = self.context['response']['data']['flowNo']  # nodeName
        self.context['session']['nodeCode'] = node_code
        self.context['session']['nodeNo'] = node_no
        self.context['session']['flowNo'] = flow_no
