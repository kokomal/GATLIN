# coding = utf-8

# A<--B<--C<--D
# A<--D
# A:B,C:D,B:C,A:D
# should return A--B,C,D | B--C,D | C--D | D--nil


# 遍历一遍获取所有集合all_members和一度关系图one_level_map，此2map此后均不会变
def prepare(raw):
    all_members = set()
    one_level_mp = {}  # key = main-character, val = follower
    pairs = raw.split(",")
    for pair in pairs:
        kvs = pair.split(":")
        k = kvs[0]
        v = kvs[1]
        all_members.add(k)
        all_members.add(v)
        if k in one_level_mp:
            ss = one_level_mp[k]
            ss.add(v)
            one_level_mp[k] = ss
        else:
            ss = set(v)
            one_level_mp[k] = ss
    return all_members, one_level_mp


def douyin(raw):
    all_members, one_level_mp = prepare(raw)
    print(all_members)
    print(one_level_mp)
    total_friends = {}
    for one in all_members:
        total_friends[one] = set()
        if one not in one_level_mp:
            continue
        allowable = set(all_members) - set(one)
        total_friends[one] = dfs(one, allowable, one_level_mp)
    print(total_friends)


def dfs(start_node, allowable_sets, one_level_map):
    if len(allowable_sets) == 0:
        return set()
    if start_node not in one_level_map or len(one_level_map[start_node]) == 0:
        return set()
    friends = one_level_map[start_node]
    next_allowable = allowable_sets.difference(friends)
    ret = set(friends)
    for friend in friends:
        ret = ret.union(dfs(friend, next_allowable, one_level_map))
    return ret


if __name__ == '__main__':
    douyin("A:B,C:D,B:C,A:D")
    # setA = set('A')
    # setB = set('A')
    # print(setA.difference(setB))
