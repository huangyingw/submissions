import random


class Solution:
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        return random.choice([i for i in range(len(self.nums)) if self.nums[i] == target])
