import random


class Solution(object):
    def __init__(self, nums):
        self.origin = list(nums)
        self.curr = list(nums)
        self.size = len(nums)

    def reset(self):
        self.curr = list(self.origin)
        return self.curr

    def shuffle(self):
        for i in range(self.size):
            pos = random.randint(0, i)
            self.curr[i], self.curr[pos] = self.curr[pos], self.curr[i]
        return self.curr
