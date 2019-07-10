
import random


class Solution(object):
    def __init__(self, nums):
        self.original = nums
        self.cur = list(nums)

    def reset(self):
        self.cur = list(self.original)
        return self.cur

    def shuffle(self):
        for i in range(1, len(self.cur)):
            n = random.randint(0, i)
            self.cur[i], self.cur[n] = self.cur[n], self.cur[i]
        return self.cur
