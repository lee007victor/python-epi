# Compute binary tree nodes in order of increasing depth
from collections import deque

def tree_depth_order(tree):
    nodes = deque([tree])
    cur_num = len(nodes)
    cur_level = []
    ret = []

    while nodes:
        if cur_num > 0:
            cur_node = nodes.popleft()
            cur_level.append(cur_node)
            nodes.append(cur_node.left)
            nodes.append(cur_node.right)
            cur_num -= 1
        else:
            cur_num = len(cur_level)
            if cur_level:
                ret.append(cur_level)
                cur_level[:] = []

    return ret
