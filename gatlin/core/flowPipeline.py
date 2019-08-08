# coding = utf-8
import copy
import json

import gatlin.infra.commonUtils as util
import gatlin.infra.print as pt
import gatlin.nodes.parserSelector as ps


# 读取需要进行测试的flow全集
def launch_flows_config(location):
    flowJsonFile = location
    with open(flowJsonFile) as fl:
        flowsConfig = json.loads(fl.read())
    return flowsConfig


def parse_one_flowX(flow_name, nodes, environ, init_param):
    pt.print_green('*' * 45 + ('PARSING %s' % flow_name) + ' BEGIN' + '*' * 45)
    context = {}
    context['environ'] = copy.deepcopy(environ)  # environ抽到全局main-flow
    context['request'] = {}
    context['response'] = {}
    context['session'] = init_param
    context['misc'] = {'canProceed': True}
    for node in nodes:
        util.inject_all(context['environ'], node)
        node_parser = ps.fetch_parser(node['nodeName'])(context)
        node_parser.lock_and_load()
        if not node_parser.can_proceed():
            pt.print_yellow("DUE TO [==%s==] THE FLOW HAS TO STOP." % context['misc']['reason'])
            pt.print_yellow('#' * 35 + "NODE %s CANNOT PROCEED" % node['nodeName'] +  '#' * 35)
            pt.print_red('*' * 45 + ('PARSING %s' % flow_name) + ' ABORTED' + '*' * 45)
            break
        context['environ'] = copy.deepcopy(environ)  # 每次清洗environ防止前后的污染，而session由node来管理
        context['request'] = {}
        context['response'] = {}
    pt.print_green('*' * 45 + ('PARSING %s' % flow_name) + ' ENDED' + '*' * 45)


if __name__ == '__main__':
    print(launch_flows_config("../input/flows.json"))
