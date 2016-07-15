# Build a minimum height BST from a sorted array.
def min_height_bst(a):
    return helper(a, 0, len(a))

def helper(a, l, r):
    if l >= r:
        return None
    m = l + (r - l)/2
    return BstNode(a[m].val, helper(a, l, m), helper(a, m + 1, r))
