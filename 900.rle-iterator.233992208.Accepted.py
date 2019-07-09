_author_ = 'jake'
_project_ = 'leetcode'
















class RLEIterator(object):
    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.encoding = A
        self.length = len(A)
        self.i = 0

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while self.i < self.length and self.encoding[self.i] < n:
            n -= self.encoding[self.i]
            self.i += 2
        if self.i >= self.length:
            return -1
        self.encoding[self.i] -= n
        return self.encoding[self.i + 1]
