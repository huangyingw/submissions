class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        start, result = 0, 1
        for end in range(1, len(nums)):
            if nums[end - 1] >= nums[end]:
                start = end
            result = max(result, end - start + 1)
        return result
