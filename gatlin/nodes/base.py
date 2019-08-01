# coding = utf-8
import json
from abc import abstractmethod, ABCMeta

import gatlin.infra.commonUtils as util
import gatlin.infra.textParser as tx
# 节点 接口
from gatlin import Gatlin
from gatlin.infra.orm import ORM
from gatlin.preps import consts


class AbstractNodeParser(metaclass=ABCMeta):
    def __init__(self, context):
        self.context = context

    @abstractmethod
    def prepare(self):
        pass

    # 具体DB的校验
    # 注意json的sql里面，where语句要加单引号
    def verify_db(self):
        print(">" * 18, "ENTER DB CHECK!", "<" * 18)
        ENV = self.context['environ']['env']
        orm = ORM(ENV)
        dbQueries = self.context['environ']['dbQueries']
        dbCriteria = self.context['environ']['dbCriteria']
        for i in range(len(dbQueries)):
            dbQuery = dbQueries[i]
            dbCriterion = dbCriteria[i]
            injectedDbQuery = injectMap(dbQuery, self.context['session'])
            injectedDbCriterion = injectMap(dbCriterion, self.context['session'])
            res = orm.assertOneRow(injectedDbQuery, injectedDbCriterion)
            if not res:
                self.context['misc']['reason'] = 'DB Check Failed'
                info = 'query=%s, criterion=%s' % (
                    str(injectedDbQuery), str(injectedDbCriterion))
                print('FAILED, info is %s' % info)
                return False
        print(">" * 18, "PASS DB CHECK!", "<" * 18)
        return True

    # 具体Response结果的解析
    def verify_response(self):
        print(">" * 18, "ENTER RESPONSE CHECK!", "<" * 18)
        expectedKeys = self.context['environ']['expectedRespKeys']
        if expectedKeys is None:
            return True
        expectedVals = self.context['environ']['expectedRespVals']
        for i in range(len(expectedKeys)):
            expectedKey = tx.inject(expectedKeys[i], '{$', '$}', self.context['session'])
            expectedVal = tx.inject(expectedVals[i], '{$', '$}', self.context['session'])
            valInRealResp = util.findCascadedMap(expectedKey, self.context['response'])
            print("valInRealResp is", valInRealResp, " WHILE expectedVal is", expectedVal)
            if "" == valInRealResp or not expectedVal == valInRealResp:
                self.context['misc']['reason'] = 'No RESP K:%s V:%s Found' % (expectedKey, expectedVal)
                return False
        print(">" * 18, "PASS RESPONSE CHECK!", "<" * 18)
        return True

    # 核心流程
    def lock_and_load(self):
        self.prepare()
        self.call_out()
        self.fetch_resp()
        should_verify = self.context['environ']['shouldVerify']  # 是否校验
        verify_way = self.context['environ']['verifyWay']  # 校验方式
        if "Y" == should_verify:
            print("NODE [%s] SHOULD-VERIFY AND VERIFY-WAY IS [%s]" % (self.context['environ']['nodeName'], verify_way))
            db_check_result = True
            resp_check_result = True
            if "db" == verify_way:
                db_check_result = self.verify_db()
            elif "resp" == verify_way:
                resp_check_result = self.verify_response()
            else:  # 都要检验
                db_check_result = self.verify_db()
                resp_check_result = self.verify_response()
            verify_result = db_check_result and resp_check_result
            self.context['misc']['canProceed'] = verify_result
        else:
            # 不应该校验，直接pass
            print("NO-VERIFY")
            self.context['misc']['canProceed'] = True

    def pack_method(self, req_param):
        METHOD = self.context['environ']['nodeName']
        req_param['method'] = consts.getMethod(METHOD)

    # 外调发起post请求
    def call_out(self):
        ENV = self.context['environ']['env']
        METHOD = self.context['environ']['nodeName']
        urlStr = consts.getEnviron(ENV) + consts.getMethod(METHOD)
        res = Gatlin.myJsonPost(urlStr, self.context['request'])
        self.context['response'] = json.loads(res.text)

    # 能否继续
    def can_proceed(self):
        return self.context['misc']['canProceed']


# 将mp的KV里面带通配符包裹的字段转换，字段的来源为sess
def injectMap(mp, sess):
    newMap = {}
    for (k, v) in mp.items():
        k = tx.inject(k, '{$', '$}', sess)
        v = tx.inject(v, '{$', '$}', sess)
        newMap[k] = v
    return newMap
