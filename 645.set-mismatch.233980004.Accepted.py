_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            if nums[abs(num) - 1] < 0:
                duplicate = abs(num)
            else:
                nums[abs(num) - 1] *= -1
        for i, num in enumerate(nums):
            if num > 0:
                missing = i + 1
                break
        return [duplicate, missing]
