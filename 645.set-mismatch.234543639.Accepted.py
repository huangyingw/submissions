
class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        once = set(nums)
        sum_whole = sum(range(len(nums) + 1))
        sum_once = sum(once)
        sum_all = sum(nums)
        dupicated = sum_all - sum_once
        left = sum_whole - sum_once
        return [dupicated, left]
