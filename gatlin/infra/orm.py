# coding = utf-8
# !/usr/bin/python
# title			:orm.py
# description	:BASIC DATABASE ORM UTILITIES
# author			:Chen Yuanjun
# date			:20190726
# version		:1.0.0
# usage			:python orm.py
# notes			:
# python_version	:2.6.6
# ==============================================================================
import pymysql

from gatlin.config import configLocation

pymysql.install_as_MySQLdb()
import MySQLdb
import json
from gatlin.preps import consts


class ORM:
    def __init__(self, env):
        self.ENV = env
        DIR = consts.getConfigDir(env)
        dbJsonFile = configLocation.get_location() + "/" + DIR + "/" + "dbconfig.json"
        with open(dbJsonFile) as f:
            rawJson = f.read()
            self.config = json.loads(rawJson)
        print("CONFIG---", self.config)

    def selectOneFromDb(self, dbname, table, entities, join='', where='1=1'):
        db = MySQLdb.connect(self.config['url'], self.config['username'], self.config['password'], dbname,
                             charset='utf8')
        cursor = db.cursor()
        command = "SELECT %s FROM %s.%s %s WHERE %s;" % (convertToCommaSplitted(entities), dbname, table, join, where)
        print("--- EXECUTE SQL ---", command)
        cursor.execute(command)
        data = cursor.fetchone()  # 返回tuple
        cols = cursor.description  # 2D的tuple
        db.close()
        mp = {}
        if data is None:
            return mp
        for i in range(len(data)):  # 最终只返回一个map，KV分别代表字段和值
            mp[cols[i][0]] = data[i]
        return mp

    # conditions代表筛选的条件，是一个map，其中dbname为库名，table为表名，以此类推
    # criteriaMap代表应该符合的条件，例如'status'='01'之类
    def assertOneRow(self, conditions, criteriaMap):
        entities = []
        join = ''
        if 'entities' in conditions:
            entities = conditions['entities']
        if 'join' in conditions:
            join = conditions['join']
        oneMapRes = self.selectOneFromDb(conditions['dbName'], conditions['tableName'], entities, join,
                                         conditions['where'])
        print("ORM RETURN", oneMapRes)
        for k in criteriaMap.keys():
            v = criteriaMap[k]
            if not whetherContainsKV(oneMapRes, k, v):
                print("NOT FIT!")
                return False
        return True


def selectAllFromDb(dbname, table, entities, join='', where='1=1'):
    db = MySQLdb.connect("localhost", "root", "1234", dbname, charset='utf8')
    cursor = db.cursor()
    command = "SELECT %s FROM %s.%s %s WHERE %s" % (convertToCommaSplitted(entities), dbname, table, join, where)
    print("SQL=", command)
    cursor.execute(command)
    data = cursor.fetchall()  # 返回tuple集合
    db.close()
    schm = cursor.description
    schema = []
    size = len(schm)
    for i in range(size):
        schema.append(schm[i][0])
    mp = {}
    mp['schema'] = schema
    mp['datas'] = data
    return mp  # 最终返回一个复杂的map，schema代表字段的列表，datas代表元组列表


def convertToCommaSplitted(entities):
    if entities is None:
        return '*'
    size = len(entities)
    if size == 0:
        return '*'
    elif size == 1:
        return entities[0]
    ret = ''
    for i in range(size - 1):
        ret = ret + entities[i] + ','
    return ret + entities[size - 1]


# 单行数据是否有KV对
def whetherContainsKV(mp, key, val):
    return key in mp and (mp[key] == val)


# 多行结果数据是否有KV对
def whetherContainsKVinArray(schema, datas, key, val):
    try:
        idx = schema.index(key)
    except ValueError:
        return False
    dtSize = len(datas)
    for i in range(dtSize):
        if datas[i][idx] == val:
            return True
    return False
