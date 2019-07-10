class Solution:
    def subsets(self, nums):
        result = [[]]
        for num in nums:
            ret = [temp + [num] for temp in result]
            result.extend(ret)
        return result
