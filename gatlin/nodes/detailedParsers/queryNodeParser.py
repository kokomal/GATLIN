# coding = utf-8

import gatlin.infra.commonUtils as util
import gatlin.infra.security as sec
import gatlin.preps.geo as geo
from gatlin.nodes.base import AbstractNodeParser
from gatlin.preps import params
import json

class SummaryQueryNodeParser(AbstractNodeParser):
    def prepare(self):
        reqParam = params.genericPackParam()
        self.pack_method(reqParam)
        biz = {}
        reqParam['userNo'] = self.context['session']['userNo']
        reqParam["bizContent"] = str(biz)  # 业务数据
        self.context['request'] = reqParam  # 归根到底目的是为了拼装request参数

    # 重点在此处理session
    def fetch_resp(self):
        print('RESP OF CURRENT NODE', json.dumps(self.context['response']))

