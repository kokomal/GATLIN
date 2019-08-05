# coding = utf-8
from gatlin.nodes.detailedParsers.demo1Parser import Demo1Parser
from gatlin.nodes.detailedParsers.demo2Parser import Demo2Parser
from gatlin.nodes.detailedParsers.demo3Parser import Demo3Parser
from gatlin.nodes.detailedParsers.loginNodeParser import LoginNodeParser
from gatlin.nodes.detailedParsers.queryNodeParser import QueryNodeParser
from gatlin.nodes.detailedParsers.registerNodeParser import RegisterNodeParser

# 所有的node
parserFactory = {'login': LoginNodeParser, 'register': RegisterNodeParser, 'query': QueryNodeParser,
                 "demo1": Demo1Parser, "demo2": Demo2Parser, "demo3": Demo3Parser}


def fetch_parser(node):
    return parserFactory[node]
