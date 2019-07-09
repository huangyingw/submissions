_author_ = 'jake'
_project_ = 'leetcode'









from collections import deque


class HitCounter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time_diff = 300
        self.q = deque()

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.q.append(timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self.q and timestamp - self.q[0] >= self.time_diff:
            self.q.popleft()
        return len(self.q)


class HitCounter2(object):
    def __init__(self):
        self.time_diff = 300
        self.q = deque()
        self.count = 0

    def hit(self, timestamp):
        if self.q and self.q[len(self.q) - 1][0] == timestamp:
            self.q[len(self.q) - 1][1] += 1
        else:
            self.q.append([timestamp, 1])
        self.count += 1

    def getHits(self, timestamp):
        while self.q and timestamp - self.q[0][0] >= self.time_diff:
            _, num = self.q.popleft()
            self.count -= num
        return self.count
