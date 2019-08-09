# coding = utf-8
import os

from openpyxl import load_workbook

import gatlin.core.flowPipeline as fl
import gatlin.infra.excel as ex
import gatlin.infra.print as pt
import gatlin.preps.geo as geo
import gatlin.preps.device as dv
cache_nodes = {}
fn = os.path.dirname(os.path.abspath(__file__)) + '/command.xlsm'


def preload():
    wb = load_workbook(fn)
    xlsm_wrap = ex.XlsmWrapper(fn)
    for ws in wb.worksheets:
        if ws.title not in ('main-flow', 'example'):
            cache_nodes[ws.title] = ex.read_sheet_and_get_json(fn, ws.title, "B3")
    return xlsm_wrap


def fire_away(xlsm_wrap):
    init_param_map = xlsm_wrap.find_row_and_pack_map('main-flow', 'initParam', 'A1')
    environ_map = xlsm_wrap.find_row_and_pack_map('main-flow', 'environ', 'A1')
    running_flows_map = xlsm_wrap.find_row_and_pack_map('main-flow', 'runningFlows', 'D1')
    dev = xlsm_wrap.find_row_and_pack_map('main-flow', 'device', 'L1')
    geo = xlsm_wrap.find_row_and_pack_map('main-flow', 'geo', 'L1')
    print('DEV', dev)
    print('GEO', geo)
    for (flow, status) in running_flows_map.items():
        if status == 'ON':
            flow_seq_map = xlsm_wrap.find_row_and_pack_map('main-flow', flow, 'G1')
            node_names = flow_seq_map.values()
            nodes = []
            for node in node_names:
                node_map = cache_nodes[node]  # 获得预先存储的node配置
                nodes.append(node_map)
            fl.parse_one_flowX(flow, nodes, environ_map, init_param_map)


if __name__ == '__main__':
    pt.print_test()
    xlsm_wrap = preload()
    fire_away(xlsm_wrap)
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
