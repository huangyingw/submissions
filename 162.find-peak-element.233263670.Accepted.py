_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] >= nums[mid + 1] and nums[mid] >= nums[mid - 1]:
                return mid
            if nums[mid + 1] > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        if nums[left] >= nums[right]:
            return left
        return right
