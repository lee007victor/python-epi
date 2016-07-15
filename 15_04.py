# Compute the LCA in a BST
def find_lca(r, n1, n2):
    min_val, max_val = min(n1.data, n2.data), max(n1.data, n2.data)
    while (r.data < min_val or r.data > max_val):
        while r.data < min_val:
            r = r.right
        while r.data > max_val:
            r = r.left
    return r
