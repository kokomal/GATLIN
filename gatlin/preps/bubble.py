# coding = utf-8


def bubble(arr):
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
    return arr


class TreeNode:
    def __init__(self, val, left_node=None, right_node=None):
        self.left_node = left_node
        self.right_node = right_node
        self.val = val

    def shadow_string(self):
        shadow = ""
        if self.left_node:
            shadow = shadow + self.left_node.shadow_string()
        shadow = shadow + str(self.val)
        if self.right_node:
            shadow = shadow + self.right_node.shadow_string()
        return shadow

    def height(self):
        return 1 + max(0 if not self.right_node else self.right_node.height(),
                       0 if not self.left_node else self.left_node.height())


def prepare_tree():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node9 = TreeNode(9)
    node4.left_node = node6
    node9.right_node = node4
    node5.right_node = node7
    node3.left_node = node9
    node3.right_node = node2
    node1.left_node = node5
    node1.right_node = node3
    return node1


if __name__ == '__main__':
    L = [4, 9, 10, 5, 111, 3, 244]
    print(bubble(L))
    print(L)
    root = prepare_tree()
    print(root.shadow_string())
    print(root.height())
