# Implement a queue using stacks.
class Queue:
    def __init__(self):
        self.push_stack = []
        self.pop_stack = []
    def enqueue(self, x):
        self.push_stack.append(x)
    def dequeue(self):
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
        if self.pop_stack:
            return self.pop_stack.pop()
