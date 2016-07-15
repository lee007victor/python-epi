# Test if a binary tree is symmetric.
def is_sysmetric(t):
    return (not t or helper(t.left, t.right))

def helper(t1, t2):
    if (not t1 and not t2):
        return True
    elif (t1 and t2):
        return (t1.data == t2.data and 
                helper(t1.left, t2.right) and helper(t1.right, t2.left))
    return False
