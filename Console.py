# coding = utf-8
import json
import os

from openpyxl import load_workbook

import gatlin.core.flowParser as fl
import gatlin.infra.excel as ex
import gatlin.infra.print as pt

cache_nodes = {}


def preload():
    fn = os.path.dirname(os.path.abspath(__file__)) + '/command.xlsm'
    wb = load_workbook(fn)
    for ws in wb.worksheets:
        if not ws.title == 'main-flow':
            cache_nodes[ws.title] = ex.read_sheet_and_get_json(fn, ws.title, "B3")


def fire_away():
    fn = os.path.dirname(os.path.abspath(__file__)) + '/command.xlsm'
    init_param_start_region = ex.find_row_region(fn, 'main-flow', 'initParam', 'A1')
    init_param_map = ex.read_selected_rows(fn, 'main-flow', init_param_start_region)
    environ_start_region = ex.find_row_region(fn, 'main-flow', 'environ', 'A1')
    environ_map = ex.read_selected_rows(fn, 'main-flow', environ_start_region)
    running_flows_start_region = ex.find_row_region(fn, 'main-flow', 'runningFlows', 'D1')
    running_flows_map = ex.read_selected_rows(fn, 'main-flow', running_flows_start_region)
    for (flow, status) in running_flows_map.items():
        if status == 'ON':
            flow_seq_map_start = ex.find_row_region(fn, 'main-flow', flow, 'G1')
            flow_seq_map = ex.read_selected_rows(fn, 'main-flow', flow_seq_map_start)
            node_names = flow_seq_map.values()
            for node in node_names:
                node_map = cache_nodes[node]  # 获得预先存储的node配置
                print(node_map)


# 开火
def fire():
    flowsConfig = fl.launch_flows_config(os.path.dirname(os.path.abspath(__file__)) + '/gatlin/input/flows.json')
    seqs = flowsConfig['flows']
    for seq in seqs:
        flowJsonFile = os.path.dirname(os.path.abspath(__file__)) + '/gatlin/input/flows/' + seq + '.json'
        with open(flowJsonFile) as fjf:
            flow = json.loads(fjf.read())
            pt.print_green("START TO PARSE %s" % flow['case'])
            fl.parse_one_flow(flow)
            pt.print_green("FINISHED PARSING %s" % flow['case'])


if __name__ == '__main__':
    preload()
    # x = input("Press Any Key To Continue...")
    fire_away()
    # pt.printGreen('print_green:Gree Color Text')
    # pt.printRed('print_red:Red Color Text')
    # pt.printYellow('print_yellow:Yellow Color Text')
    # pt.printYellowRed('print_yellow:Yellow Red Color Text')
