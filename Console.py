# coding = utf-8
import os

from openpyxl import load_workbook

import gatlin.core.flowPipeline as fl
import gatlin.infra.excel as ex

MAIN_FLOW = 'main-flow'

cache_nodes = {}
fn = os.path.dirname(os.path.abspath(__file__)) + '/command.xlsm'


# 初始化读取xlsm配置，保留workbook的openpyxl对象,预加载配置...
def preload():
    wb = load_workbook(fn)
    xlsm_wrap = ex.XlsmWrapper(fn)
    for ws in wb.worksheets:
        if ws.title not in (MAIN_FLOW, 'example'):
            cache_nodes[ws.title] = ex.read_sheet_and_get_json(fn, ws.title, "B3")
    return xlsm_wrap


def fire_away(xlsm_wrap):
    init_param_map = xlsm_wrap.find_row_and_pack_map(MAIN_FLOW, 'initParam', 'A1')
    environ_map = xlsm_wrap.find_row_and_pack_map(MAIN_FLOW, 'environ', 'A1')
    running_flows_map = xlsm_wrap.find_row_and_pack_map(MAIN_FLOW, 'runningFlows', 'D1')
    dev = xlsm_wrap.find_row_and_pack_map(MAIN_FLOW, 'device', 'L1')
    geo = xlsm_wrap.find_row_and_pack_map(MAIN_FLOW, 'geo', 'L1')
    person = xlsm_wrap.find_row_and_pack_map(MAIN_FLOW, 'personal_info', 'L1')
    idcard = xlsm_wrap.find_row_and_pack_map(MAIN_FLOW, 'idcard', 'P1')
    init_param_map['geo'] = geo
    init_param_map['deviceInfo'] = dev
    init_param_map['personal_info'] = person
    init_param_map['idcard'] = idcard
    for (flow, status) in running_flows_map.items():
        if status == 'ON':
            flow_seq_map = xlsm_wrap.find_row_and_pack_map_with_switch(MAIN_FLOW, flow, 'G1')
            node_names = flow_seq_map.values()
            nodes = []
            for node in node_names:
                node_map = cache_nodes[node]  # 获得预先存储的node配置
                nodes.append(node_map)
            fl.parse_one_flowX(flow, nodes, environ_map, init_param_map)


if __name__ == '__main__':
    # pt.print_test()
    xlsm_wrap = preload()
    fire_away(xlsm_wrap)
    while 1:
        x = input("Press [q] to Quit. Press Any Other Key To RESTART...")
        if x != 'q':
            preload()
            fire_away()
        else:
            break
