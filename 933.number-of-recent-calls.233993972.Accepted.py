_author_ = 'jake'
_project_ = 'leetcode'










from collections import deque


class RecentCounter:
    def __init__(self):
        self.times = deque()
        self.WINDOW = 3000

    def ping(self, t):

        self.times.append(t)
        while t - self.times[0] > self.WINDOW:
            self.times.popleft()
        return len(self.times)
