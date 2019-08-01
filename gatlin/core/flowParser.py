# coding = utf-8
import copy
import json

import gatlin.infra.commonUtils as util
import gatlin.nodes.parserSelector as ps


# 读取需要进行测试的flow全集
def launch_flows_config(location):
    flowJsonFile = location
    with open(flowJsonFile) as fl:
        flowsConfig = json.loads(fl.read())
    return flowsConfig


def parse_one_flow(input_flow_map):
    caseName = input_flow_map['case']
    print('*' * 40, 'PARSING %s' % caseName, 'BEGIN', '*' * 40)
    context = {}
    context['environ'] = copy.deepcopy(input_flow_map['environ'])
    context['initParam'] = input_flow_map['initParam']
    context['request'] = {}
    context['response'] = {}
    context['session'] = {}
    context['misc'] = {'canProceed': True}
    nodes = input_flow_map['nodes']
    for node in nodes:
        util.inject_all(context['environ'], node)
        nodeParser = ps.fetch_parser(node['nodeName'])(context)
        nodeParser.lock_and_load()
        if not nodeParser.can_proceed():
            print("DUE TO [==%s==] THE FLOW HAS TO STOP." % context['misc']['reason'])
            print('#' * 30, "NODE %s CANNOT PROCEED" % node['nodeName'], '#' * 30)
            break
        context['environ'] = copy.deepcopy(input_flow_map['environ'])  # 每次清洗environ防止前后的污染，而session由node来管理
    print('*' * 40, 'PARSING %s' % caseName, 'ENDED', '*' * 40)


if __name__ == '__main__':
    print(launch_flows_config("../input/flows.json"))
