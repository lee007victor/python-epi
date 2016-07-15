# singly linked list
class Node(object):
    
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList(object):
    
    def __init__(self, head=None):
        self.head = head


def merge_two_lists(l1, l2):
    Node dummy_head = None
    Node tail = dummy_head

    while l1 and l2:
        append_node([l1, l2][l1.data > l2.data], tail)

    tail.next = l1 if l1 else l2

    return dummy_head.next


def append_node(node, tail):
    tail.next = node
    tail = node
    node = node.next_node

# doubly linked list
class Node(object):

    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


def merge_two_lists(l1, l2):
    Node dummy_head = None
    Node new_head = dummy_head

    while l1 and l2:
        append_node([l1, l2][l1.data > l2.data], new_head)

    new_head = l1 if l1 else l2

    return dummy_head.next


def append_node(node, head):
    head.next = node
    node.prev_node = head
    head = node
    node = node.next_node
