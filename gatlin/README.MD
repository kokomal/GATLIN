# 集成测试框架GATLIN文档
作者：		陈元俊
版本：		1.0.0
时间：		2019-07-15
********************************
## 基本开发运行环境
开发运行环境： 	Python 3.7.3
OS:			Win10 64
依赖库：		基本py3的模块，需要额外依赖
			1.requests;
			2.pycryptodome
			版本细节参见requirements.txt
			3.MySQLdb
			
if you want to use MySQLdb first you have to install pymysql on your pc by typing in cmd of windows

    pip install pymysql
then in python shell, type

    import pymysql
    pymysql.install_as_MySQLdb()
    import MySQLdb
    db = MySQLdb.connect("localhost" , "root" , "password")
this will establish the connection.
********************************
## 设计思想
为了解决手动测试的痛点（环境频繁切换，请求参数拼装繁杂
易错，加密请求），减少重复手工劳动，提升效率；此外，
为了满足测试过程的自动化衔接，需要将出参的参数再次传入
下一个入参，进行串行的动态测试。本框架参考了已有的自动化
测试工具，并且结合具体业务场景，给出了基本的代码框架。
后续可以根据实际需求进一步进行扩展。
********************************
## 核心代码和库说明

********************************
## 使用方法

