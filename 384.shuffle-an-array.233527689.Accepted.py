import random


class Solution(object):
    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums

    def shuffle(self):
        result = self.nums[:]
        for i in range(len(result)):
            swap = random.randint(i, len(result) - 1)
            result[i], result[swap] = result[swap], result[i]
        return result
