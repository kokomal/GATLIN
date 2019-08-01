# coding = utf-8

from gatlin.nodes.base import AbstractNodeParser


class QueryNodeParser(AbstractNodeParser):
    def verify_db(self):
        return True

    def verify_response(self):
        self.context['misc']['reason'] = 'REMOTE ERROR'
        return False

    def lock_and_load(self):
        self.context['token'] = "9999999999999"
        print("Query!")
