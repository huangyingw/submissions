class Solution(object):
    def missingNumber(self, nums):
        res = len(nums)
        for i, v in enumerate(nums):
            res ^= i
            res ^= v
        return res
