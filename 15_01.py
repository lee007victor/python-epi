# Test if a binary tree satisfies the BST property
import sys

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 1:
def is_bst(tree):
    return is_key_in_range(tree, sys.maxint, -sys.maxint - 1)

def is_key_in_range(node, upper, lower):
    if not node:
        return True
    if node.val < lower or node.val > upper:
        return False
    return (is_key_in_range(node.left, node.val, lower) and 
            is_key_in_range(node.right, upper, node.val))

# Solution 2: bfs, in-order traversal
import collections

# QueueEntry: (node, lower, upper)

def is_bst(tree):
    queue = collections.deque([])
    queue.append((tree, -sys.maxint - 1, sys.maxint))

    while queue:
        node, lower, upper = queue.popleft()
        while node:
            if node.val > upper or node.val < lower:
                return False
            queue.append((node.left, lower, node.val))
            queue.append((node.right, ndoe.val, upper))

    return True
