# coding = utf-8
def inject_all(target, src):
    for (k, v) in src.items():
        target[k] = v

def inject_all_soft(target, src):
    for (k, v) in src.items():
        if v is None or v == "":
            continue
        target[k] = v

def findCascadedMap(complex_key, target_map):
    if ">" not in complex_key:
        if complex_key in target_map:
            return target_map[complex_key]
        else:
            return ""
    keysArr = complex_key.split(">")
    iterMap = target_map
    for key in keysArr:
        if key in iterMap:
            nextOne = iterMap[key]
            if type(nextOne) == dict:
                iterMap = nextOne
                continue
            else:
                return nextOne
        else:
            return ""
