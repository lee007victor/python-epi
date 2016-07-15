# Implement even-odd merge.
def odd_even_merge(head):
    if not head:
        return head
    even_dummy_head, odd_dummy_head = ListNode(0, None), ListNode(0, None)
    tails = [even_dummy_head, odd_dummy_head]
    cur_node, turn = head, 0 
    while cur_head:
        tails[turn].next = cur_node
        cur_node = cur_node.next
        turn ^= 1
    tails[0].next, tails[1].next = odd_dummy_head.next, None
    return even_dummy_head.next
