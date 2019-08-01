# coding = utf-8
import json


def inject(rawStr, pre, after, kvMap):
    cur = rawStr
    while 1:
        try:
            pos1 = cur.index(pre)
            pos2 = cur.index(after)
            tobeRep = cur[pos1 + 2: pos2]
            tobeNew = kvMap[tobeRep]
            cur = cur[0:pos1] + str(tobeNew) + cur[pos2 + 2:]
        except:
            return cur


def get_pretty_print(json_object):
    return json.dumps(json_object, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)


if __name__ == '__main__':
    kvMap = {"world": "popo", "var": 123}
    print("res---", inject("haha{$world$}, I have {$var$} cents", '{$', '$}', kvMap))
    print("res---", inject("haha{$world$}, I have {#var#} cents", '{#', '#}', kvMap))
