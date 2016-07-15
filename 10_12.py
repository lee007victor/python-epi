# Reconstruct a binary tree from traversal data.
def reconstruct_tree(list_pre, list_in):
    n2i_in = {}
    for i in range(len(list_in)):
        n2i_in[list_in[i]] = i
    return helper(list_pre, 0, len(list_pre), 0, len(list_in), n2i_in)

def helper(list_pre, m_pre, n_pre, m_in, n_in, n2i_in):
    if (m_pre >= n_pre or m_in >= n_in):
        return None
    r_in = n2i_in[list_pre[m_pre]]
    size_l = r_in - m_pre
    return TreeNode(
        list_pre[m_pre],
        helper(list_pre, m_pre + 1, m_pre + 1 + size_l, m_in, r_in, n2i_in),
        helper(list_in, m_pre + 1 + size_l, n_pre, r_in + 1, n_in, n2i_in))
