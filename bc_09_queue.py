class MyQueue:
    def __init__(self):
        self.container = []

    def is_empty(self):
        return self.container == []

    def size(self):
        return len(self.container)

    def front(self):
        if self.is_empty():
            return None
        return self.container[-1]

    def back(self):
        if self.is_empty():
            return None
        return self.container[0]

    def push(self, item):
        self.container.insert(0, item)

    def pop(self):
        self.container.pop()

q = MyQueue()
print q.is_empty()
print q.size()
q.push(0)
q.push(1)
q.push(2)
print 'Front:'
print q.front()
print 'Back:'
print q.back()
q.pop()
print 'New Front:'
print q.front()
print 'New Back:'
print q.back()
