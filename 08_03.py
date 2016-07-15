# Test for cyclicity.
def has_cycle(head):
    fast, slow = head, head
    while (fast and slow):
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            cyc_len = 1
            fast = fast.next
            while slow != fast:
                cyc_len += 1
                fast = fast.next
            iter_a = head
            while cyc_len > 0:
                iter_a = iter_a.next
                cyc_len -= 1 
            iter_b = head
            while iter_a != iter_b:
                iter_a = iter_a.next
                iter_b = iter_b.next
            return iter_a

    return None
