# Implement a circular queue.
class Queue:
    def __init__(self, cap):
        self.q = [None] * cap
        self.head = 0
        self.tail = 0
        self.length = 0

    def enque(n):
        if self.length == len(self.q):
            self.q += [None] * len(self.q)
        self.q[self.tail] = n
        self.tail = (self.tail + 1) % len(self.q)
        self.length += 1

    def deque():
        if self.length > 0:
            ret = self.q[self.head]
            self.head = (self.head - 1) % len(self.q)
            self.length -= 1
            return ret
        # raise error if self.length <= 0

    def size():
        return self.length
