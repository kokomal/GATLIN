# coding = utf-8
from gatlin.nodes.detailedParsers.demo1Parser import Demo1Parser
from gatlin.nodes.detailedParsers.demo2Parser import Demo2Parser
from gatlin.nodes.detailedParsers.demo3Parser import Demo3Parser
from gatlin.nodes.detailedParsers.itemCommitNodeParser import ItemCommitNodeParser, IdcardUploadNodeParser, \
    TradePwdNodeParser, ItemCommitIdNodeParser, ItemCommitNodeFaceParser, PersonInfoNodeParser
from gatlin.nodes.detailedParsers.loginNodeParser import LoginNodeParser
from gatlin.nodes.detailedParsers.queryNodeParser import SummaryQueryNodeParser
from gatlin.nodes.detailedParsers.registerNodeParser import RegisterNodeParser

# 所有的node
parserFactory = {'login': LoginNodeParser, 'register': RegisterNodeParser,
                 "demo1": Demo1Parser, "demo2": Demo2Parser, "demo3": Demo3Parser,
                 "summaryQuery": SummaryQueryNodeParser,
                 "itemCommit": ItemCommitNodeParser, "itemCommitFace": ItemCommitNodeFaceParser,
                 "idcardUpload": IdcardUploadNodeParser,
                 "tradePwd": TradePwdNodeParser, "itemCommitId": ItemCommitIdNodeParser,
                 "itemCommitPersonInfo": PersonInfoNodeParser}


def fetch_parser(node):
    return parserFactory[node]
