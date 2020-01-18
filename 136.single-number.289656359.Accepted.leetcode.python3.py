class Solution:
    def singleNumber(self, nums):
        res = 0
        for no in nums:
            res ^= no
        return res
