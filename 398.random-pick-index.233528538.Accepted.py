_author_ = 'jake'
_project_ = 'leetcode'











import random


class Solution(object):
    def __init__(self, nums):

        self.nums = nums

    def pick(self, target):

        count = 0
        for i, num in enumerate(self.nums):
            if num == target:
                if random.randint(0, count) == 0:
                    result = i
                count += 1
        return result
