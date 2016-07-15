# Reverse a single sublist.
class ListNode:
    def __init__(self, data=None, next=None):
        self.data = None
        self.next = None

def reverse_sublist(l, s, f):
    if s == f:
        return l
    dummy = ListNode(None, l)
    sub_head = dummy
    i = 1
    while i < s:
        sub_head = sub_head.next
        i += 1
    sub_iter = sub_head.next
    while s < f:
        temp = sub_iter.next
        sub_iter.next = temp.next
        temp.next = sub_head.next
        sub_head.next = temp
        s += 1
    return dummy.next

