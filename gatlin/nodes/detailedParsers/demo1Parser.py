# coding = utf-8

from gatlin.nodes.base import AbstractNodeParser


class Demo1Parser(AbstractNodeParser):
    def prepare(self):
        print("Demo1")

    # 重点在此处理session
    def fetch_resp(self):
        print("Demo1 Ends")
