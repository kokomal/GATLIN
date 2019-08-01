# coding = utf-8
from gatlin.nodes.detailedParsers.loginNodeParser import LoginNodeParser
from gatlin.nodes.detailedParsers.queryNodeParser import QueryNodeParser
from gatlin.nodes.detailedParsers.registerNodeParser import RegisterNodeParser

# 所有的node
parserFactory = {'login': LoginNodeParser, 'register': RegisterNodeParser, 'query': QueryNodeParser}


def fetch_parser(node):
    return parserFactory[node]
