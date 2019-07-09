class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for num in nums:
            ret = [temp + [num] for temp in result]
            result.extend(ret)
        return result
