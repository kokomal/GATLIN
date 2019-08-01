# coding = utf-8

from gatlin.nodes.base import AbstractNodeParser


class RegisterNodeParser(AbstractNodeParser):
    def verify_db(self):
        return True

    def verify_response(self):
        return True

    def lock_and_load(self):
        self.context['token'] = "9999999999999"
        print("Register!")
