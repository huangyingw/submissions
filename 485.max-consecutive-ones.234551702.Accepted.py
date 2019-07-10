
from itertools import groupby


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        r = [len(list(g)) for k, g in groupby(nums) if k == 1]
        return 0 if len(r) == 0 else max(r)
