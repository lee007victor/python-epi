class MyStack:
    def __init__(self):
        self.container = []

    def is_empty(self):
        return self.container == []

    def size(self):
        return len(self.container)

    def push(self, item):
        self.container.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.container.pop()

    def top(self):
        if self.is_empty():
            return None
        return self.container[-1]

s = MyStack()
s.push(-1)
s.push(2)
print s.is_empty()
print s.size()
print s.pop()
print s.top()
