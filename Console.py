# coding = utf-8
import json
import os

import gatlin.core.flowParser as fl


# 开火
def fire():
    flowsConfig = fl.launch_flows_config(os.path.dirname(os.path.abspath(__file__)) + '/gatlin/input/flows.json')
    seqs = flowsConfig['flows']
    for seq in seqs:
        flowJsonFile = os.path.dirname(os.path.abspath(__file__)) + '/gatlin/input/flows/' + seq + '.json'
        with open(flowJsonFile) as fjf:
            flow = json.loads(fjf.read())
            fl.parse_one_flow(flow)


if __name__ == '__main__':
    fire()
