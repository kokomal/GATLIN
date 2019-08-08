# coding = utf-8
import os

from openpyxl import load_workbook

import gatlin.core.flowPipeline as fl
import gatlin.infra.excel as ex
import gatlin.infra.print as pt

cache_nodes = {}


def preload():
    fn = os.path.dirname(os.path.abspath(__file__)) + '/command.xlsm'
    wb = load_workbook(fn)
    for ws in wb.worksheets:
        if ws.title not in ('main-flow', 'demo'):
            cache_nodes[ws.title] = ex.read_sheet_and_get_json(fn, ws.title, "B3")


def fire_away():
    fn = os.path.dirname(os.path.abspath(__file__)) + '/command.xlsm'
    init_param_map = ex.find_row_and_pack_map(fn, 'main-flow', 'initParam', 'A1')
    environ_map = ex.find_row_and_pack_map(fn, 'main-flow', 'environ', 'A1')
    running_flows_map = ex.find_row_and_pack_map(fn, 'main-flow', 'runningFlows', 'D1')
    for (flow, status) in running_flows_map.items():
        if status == 'ON':
            flow_seq_map = ex.find_row_and_pack_map(fn, 'main-flow', flow, 'G1')
            node_names = flow_seq_map.values()
            nodes = []
            for node in node_names:
                node_map = cache_nodes[node]  # 获得预先存储的node配置
                nodes.append(node_map)
            fl.parse_one_flowX(flow, nodes, environ_map, init_param_map)


if __name__ == '__main__':
    pt.print_test()
    preload()
    fire_away()
    while 1:
        x = input("Press [q] to Quit. Press Any Other Key To RESTART...")
        if not x == 'q':
            preload()
            fire_away()
        else:
            break
    # pt.printGreen('print_green:Gree Color Text')
    # pt.printRed('print_red:Red Color Text')
    # pt.printYellow('print_yellow:Yellow Color Text')
    # pt.printYellowRed('print_yellow:Yellow Red Color Text')
