from collections import deque


class MovingAverage:
    def __init__(self, size):

        self.window = deque()
        self.size = size

    def next(self, val):

        if len(self.window) == self.size:
            self.window.popleft()
        self.window.append(val)
        return sum(self.window) / len(self.window)
