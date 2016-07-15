# Reconstruct a BST from traversal data
class BstNode:
    def __init__(self, val, l, r):
        self.val = val
        self.l = l
        self.r = r

# Preorder solution 1: O(n*log(n))
def reconstruct_bst_preorder(seq):
    return preorder_helper(seq, 0, len(seq))

def preorder_helper(seq, start, end):
    if start >= end:
        return None
    i = start + 1
    while (i < end and seq[start].val > seq[i].val):
        i += 1
    return BstNode(seq[start].val, 
                   preorder_helper(seq, start + 1, i), 
                   preorder_helper(seq, i, end))

# Postorder solution 1: O(n*log(n))
def reconstruct_bst_postorder(seq):
    return postorder_helper(seq, 0, len(seq) - 1)

def postorder_helper(seq, start, end):
    if start >= end:
        return None
    j = end - 1
    while (j >= 0 and seq[end].val > seq[j].val):
        j -= 1
    return BstNode(seq[end].val, 
                   postorder_helper(seq, start, j), 
                   postorder_helper(seq, j + 1, end - 1))


# Preorder solution 2: O(n)
import sys

root_id = 0

def reconstruct_bst_preorder(seq):
   return preorder_helper(seq, -sys.maxint - 1, sys.maxint)

def preorder_helper(seq, lower, upper):
    global root_id
    if root_id == len(seq):
        return None
    root_val = seq[root_id].val
    if (root_val < lower or root_val > upper):
        return None
    root_id += 1
    lc = preorder_helper(seq, lower, root_val)
    rc = postorder_helper(seq, root_val, upper)
    return BstNode(root_val, lc, rc)

# Postorder solution 2: O(n)
import sys

root_id = None

def reconstruct_bst_postorder(seq):
    root_id = len(seq) - 1
    return postorder_helper(seq, -sys.maxint - 1, sys.maxint)

def postorder_helper(seq, lower, upper):
    global root_id
    if root_id == -1:
        return None
    root_val = seq[root_id]
    if (root_val < lower or root_val > upper):
        return None
    root_val -= 1
    rc = postorder_helper(seq, root_val, upper)
    lc = postorder_helper(seq, lower, root_val)
    return BstNode(root_val, lc, rc)
