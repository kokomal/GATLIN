# coding = utf-8

from gatlin.nodes.base import AbstractNodeParser


class Demo2Parser(AbstractNodeParser):
    def prepare(self):
        print("Demo2")

    # 重点在此处理session
    def fetch_resp(self):
        print("Demo2 Ends")
