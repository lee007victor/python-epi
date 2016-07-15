# Compute the LCA when nodes have parent pointers.
def find_lca(n0, n1):
    d0 = find_depth(n0)
    d1 = find_depth(n1)
    if d1 < d0:
        n0, n1 = n1, n0
        d0, d1 = d1, d0
    diff_d = d1 - d0
    while diff_d:
        n1 = n1.parent
        diff_d -= 1
    while n0 != n1:
        n0, n1 = n0.parent, n1.parent
    return n0

def find_depth(n):
    d = 0
    while n.parent:
        d += 1
        n = n.parent
    return d
