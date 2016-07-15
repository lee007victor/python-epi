# Compute the LCA, optimizing for close ancestors.
def lca(n1, n2):
    visited = set([])
    while n1 or n2:
        if n1 in visited:
            return n1
        n1 = n1.p
        if n2 in visited:
            return n2
        n2 = n2.p
    # may need to return a error here.
