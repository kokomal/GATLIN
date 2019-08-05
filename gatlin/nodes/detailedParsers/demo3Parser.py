# coding = utf-8

from gatlin.nodes.base import AbstractNodeParser


class Demo3Parser(AbstractNodeParser):
    def prepare(self):
        print("Demo3")

    # 重点在此处理session
    def fetch_resp(self):
        print("Demo3 Ends")
