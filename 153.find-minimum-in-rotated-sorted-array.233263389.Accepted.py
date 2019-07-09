_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] <= nums[right]:
                break
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid


        return nums[left]
