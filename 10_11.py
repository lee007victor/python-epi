# Implement an inorder traversal with O(1) space (assume nodes have parents
# fields).
def inorder_traversal(head):
    prev, curr = None, head
    ret = []
    while curr:
        if curr.p == prev:
            if curr.l:
                _next = curr.l
            else:
                ret.append(curr.data)
                _next = curr.r if curr.r else curr.p
        elif curr.l == prev:
            ret.append(curr.data)
            _next = curr.r if curr.r else curr.p
        else:
            _next = curr.p
        prev = curr
        curr = _next
    return ret
