# Find the first key greater than a given value in a BST.
class TreeNode:
    def __init__(v=None, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r

def find_first_greater(t, k):
    sub_t, ret = t, None
    while sub_t:
        if sub_t.v > k:
            ret = sub_t.v
            sub_t = sub_t.l
        else:
            sub_t = sub_t.r
    return ret
