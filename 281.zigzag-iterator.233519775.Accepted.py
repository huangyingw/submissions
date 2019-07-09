_author_ = 'jake'
_project_ = 'leetcode'






from collections import deque


class ZigzagIterator(object):
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.vectors = [v for v in (v1, v2) if v]
        self.q = deque((i, 0) for i in range(len(self.vectors)))

    def next(self):
        """
        :rtype: int
        """
        vector, index = self.q.popleft()
        if index < len(self.vectors[vector]) - 1:
            self.q.append((vector, index + 1))
        return self.vectors[vector][index]

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.q)
