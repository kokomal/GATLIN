# coding=utf-8
# 抽取独立的参数拼装模块
import time

from gatlin.preps import device


# 通用参数map拼装
def genericPackParam():
    param = {}
    param["bizContent"] = "{}"  # 业务数据
    param["pageName"] = "index.html"
    param["timestamp"] = str(int(time.time() * 1000))
    param["charset"] = "UTF-8"
    return param


if __name__ == '__main__':
    print(genericPackParam())
