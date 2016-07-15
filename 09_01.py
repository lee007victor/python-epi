# Solution 1: O(n) space, O(1) time

class MyStack:
    def __init__(self):
        self.container = []

    def is_empty(self):
        return self.container == []

    def max(self):
        if self.is_empty():
            raise ValueError('max(): empty stack')
        return self.container[-1][1]

    def push(self, data):
        self.container.append([data, data if self.is_empty() else max(data, self.max())])

    def pop(self):
        if self.is_empty():
            raise ValueError('pop(): empty stack')
        _, ret = self.container.pop()
        return ret

# Solution 2: optimize the best base

class MyStack:
    def __init__(self):
        self.container = []
        self.max_stack = []

    def is_empty(self):
        return self.container == []

    def max(self):
        if self.is_empty():
            raise ValueError('max(): empty stack')
        return self.max_stack[-1][0]

    def push(self, data):
        self.container.append(data)
        if self.max_stack == [] or data > self.max():
            self.max_stack.append([data, 1])
        else:
            self.max_stack[-1][1] += 1

    def pop(self):
        ret = self.container.pop()
        if ret == self.max():
            self.max_stack[-1][1] -= 1
            if self.max_stack[-1][1] == 0:
                self.max_stack.pop()

