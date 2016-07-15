# Reference 1:
# https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python
# Reference 2:
# http://www.openbookproject.net/thinkcs/python/english2e/ch18.html

class Node(oject):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        cur_node = self.head
        count = 0
        while cur_node:
            count += 1
            cur_node = cur_node.get_next()
        return count

    def search(self, data):
        cur_node = self.head
        while cur_node:
            if cur_node.get_data() != data:
                cur_node = cur_node.get_next()
            else:
                return cur_node
        raise ValueError('Data not in list')

    def delete(self, data):
        cur_node = self.head
        pre_node = None
        while cur_node:
            if cur_node.get_data() != data:
                pre_node = cur_node
                cur_node = cur_node.get_next()
            else:
                if pre_node is None:
                    self.head = cur_node.get_next()
                else:
                    pre_node.set_next(cur_node.get_next())
                return
        raise ValueError('Data not in list')

