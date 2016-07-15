# Test if a binary tree is height-balanced

class Node:
    def __init__(self, val=None):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

# Solution 1: O(n) space
def check_height_balanced(root):
    sub_tree_height = {None:-1}

    def is_balanced(node):
        if node.l and not is_balanced(node.l):
            return False
        if node.r and not is_balanced(node.r):
            return False
        l_h = sub_tree_height[node.l]
        r_h = sub_tree_height[node.r]
        if abs(l_h - r_h) > 1:
            return False
        else:
            sub_tree_height[node] = max(l_h, r_h) + 1
            return True

    return is_balanced(root)

# Solution 2: reduce space
def check_height_balanced(root):
    def is_balanced(node):
        if not node:
            return (True, -1)
        l_res = is_balanced(node.l)
        if not l_res[0]:
            return (False, 0)
        r_res = is_balanced(node.r)
        if not r_res[0]:
            return (False, 0)
        ret_b = abs(l_res[1] - r_res[1]) <= 1
        ret_h = max(l_res[1], r_res[1]) + 1
        return (ret_b, ret_h)

    return is_balanced(root)[0]
