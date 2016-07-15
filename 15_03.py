# Find the k largest elements in a BST.
class TreeNode:
    def __init__(v=None, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r

def find_k_largest(tree, k):
    ret = []
    helper(tree, k, ret)
    return ret

def helper(tree, k , ret):
    if tree and len(ret) < k:
        helper(tree.r, k, ret)
        if len(ret) < k:
            ret.append(tree.v)
            helper(tree.l, k, ret)
