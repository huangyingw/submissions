


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        totalSum, n = sum(nums), len(nums)
        expectedSum = (n * (n + 1)) / 2
        return expectedSum - totalSum
