# coding = utf-8
import json

import gatlin.core.flowParser as fl


# 开火
def fire():
    flowsConfig = fl.launch_flows_config('input/flows.json')
    seqs = flowsConfig['flows']
    for seq in seqs:
        flowJsonFile = 'input/flows/' + seq + '.json'
        with open(flowJsonFile) as fjf:
            flow = json.loads(fjf.read())
            fl.parse_one_flow(flow)


if __name__ == '__main__':
    fire()
