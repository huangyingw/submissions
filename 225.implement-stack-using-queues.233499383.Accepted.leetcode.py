from collections import deque


class MyStack(object):
    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.appendleft(x)

    def pop(self):
        new_queue = deque()
        while True:
            x = self.queue.pop()
            if not self.queue:
                self.queue = new_queue
                return x
            new_queue.appendleft(x)

    def top(self):
        new_queue = deque()
        while self.queue:
            x = self.queue.pop()
            new_queue.appendleft(x)
        self.queue = new_queue
        return x

    def empty(self):
        return len(self.queue) == 0
