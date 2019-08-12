# coding = utf-8
from gatlin.nodes.detailedParsers.demo1Parser import Demo1Parser
from gatlin.nodes.detailedParsers.demo2Parser import Demo2Parser
from gatlin.nodes.detailedParsers.demo3Parser import Demo3Parser
from gatlin.nodes.detailedParsers.loginNodeParser import LoginNodeParser
from gatlin.nodes.detailedParsers.queryNodeParser import SummaryQueryNodeParser
from gatlin.nodes.detailedParsers.registerNodeParser import RegisterNodeParser
from gatlin.nodes.detailedParsers.itemCommitNodeParser import ItemCommitNodeParser

# 所有的node
parserFactory = {'login': LoginNodeParser, 'register': RegisterNodeParser,
                 "demo1": Demo1Parser, "demo2": Demo2Parser, "demo3": Demo3Parser,
                 "summaryQuery": SummaryQueryNodeParser,
                 "itemCommit": ItemCommitNodeParser}


def fetch_parser(node):
    return parserFactory[node]
