class MyStack:
    def __init__(self):
        self.stack1 = []
    def push(self, x):
        self.stack1.append(x)
    def pop(self):
        return self.stack1.pop()
    def top(self):
        return self.stack1[-1]
    def empty(self):
        return not len(self.stack1)
def __init__(self):
    self._queue = collections.deque()
def push(self, x):
    q = self._queue
    q.append(x)
def pop(self):
    return self._queue.pop()
def top(self):
    return self._queue[-1]
def empty(self):
    return len(self._queue) == 0
