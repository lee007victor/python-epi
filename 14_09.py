# Implement a fast sorting algorithm for lists.
def stable_sort_list(h):
    if not h or not h.next:
        return h
    pre, slow, fast = None, h, h
    while fast and fast.next:
        pre = slow
        slow = slow.next
        fast = fast.next.next
    pre.next = None
    return merge_list(stable_sort_list(h), stable_sort_list(slow))

def merge_list(h1, h2):
    dummy = ListNode(0, None)
    curr = dummy
    while h1 and h2:
        if h1.val <= h2.val:
            curr.next = h1
            h1 = h1.next
        else:
            curr.next = h2
            h2 = h2.next
        curr = curr.next
    curr.next = p1 if p1 else p2
    return dummy.next
