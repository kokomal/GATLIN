import unittest

import gatlin.infra.commonUtils as util
import gatlin.infra.textParser as tx
from gatlin.infra.orm import ORM


class UtilTest(unittest.TestCase):
    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('***AFTER ONE TEST***')

    def setUp(self):
        # 每个测试用例执行之前做操作wqd
        print('***BEFORE ONE TEST***')

    @classmethod
    def tearDownClass(self):
        # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        print('FINISHED...')

    @classmethod
    def setUpClass(self):
        # 必须使用@classmethod 装饰器,所有test运行前运行一次
        print('STARTING...')

    def testCascadeMapFind(self):
        demoMap = {"a": {"b": {"c": 123456}}}
        print("DEMO-MAP", tx.get_pretty_print(demoMap))
        complexKey = "a>b>c"
        print("FIND A>B>C", util.findCascadedMap(complexKey, demoMap))

        complexKey = "a>b>d"
        print("FIND A>B>D", util.findCascadedMap(complexKey, demoMap))

        complexKey = "a"
        print("FIND A(ONLY)", util.findCascadedMap(complexKey, demoMap))

    def testOrm(self):
        orm = ORM("PH_DEV")
        # retMap = orm.selectOneFromDb('lps','i_iou', [], '', "loan_req_no = 'LP6567678933669388288'")
        # print(retMap)
        conditions = {}
        conditions["entities"] = []
        conditions["join"] = ""
        conditions["dbName"] = "lps"
        conditions["tableName"] = "i_iou"
        conditions["where"] = "loan_req_no = 'LP6567678933669388288'"
        criteriaMap = {}
        criteriaMap["loan_state"] = "DS"
        print(orm.assertOneRow(conditions, criteriaMap))
