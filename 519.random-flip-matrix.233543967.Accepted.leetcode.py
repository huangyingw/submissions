import random


class Solution(object):
    def __init__(self, n_rows, n_cols):
        self.start, self.end = 0, n_rows * n_cols - 1
        self.used_to_free = {}
        self.cols = n_cols

    def flip(self):
        x = random.randint(self.start, self.end)
        index = self.used_to_free.get(x, x)
        self.used_to_free[x] = self.used_to_free.get(self.start, self.start)
        self.start += 1
        return list(divmod(index, self.cols))

    def reset(self):
        self.start = 0
        self.used_to_free = {}
