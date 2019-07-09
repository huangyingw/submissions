_author_ = 'jake'
_project_ = 'leetcode'












import random


class Solution(object):
    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.start, self.end = 0, n_rows * n_cols - 1
        self.used_to_free = {}
        self.cols = n_cols

    def flip(self):
        """
        :rtype: List[int]
        """
        x = random.randint(self.start, self.end)
        index = self.used_to_free.get(x, x)
        self.used_to_free[x] = self.used_to_free.get(self.start, self.start)
        self.start += 1
        return list(divmod(index, self.cols))

    def reset(self):
        """
        :rtype: void
        """
        self.start = 0
        self.used_to_free = {}
