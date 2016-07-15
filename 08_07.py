# Remove the k-th last element from a list
class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next 

def delete_last_k(head, k):
    dummy = ListNode(None, head)
    first = dummy.next
    while k:
        first = first.next
        k -= 1
    second = dummy
    while first:
        first, second = first.next, second.next
    second.next = second.next.next
    return dummy.next
