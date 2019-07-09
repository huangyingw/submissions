class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        currSum, result = nums[0], nums[0]
        for index in range(1, len(nums)):
            currSum = max(nums[index], currSum + nums[index])
            result = max(result, currSum)
        return result
