class Solution(object):
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        if nums[left] <= nums[right]:
            return nums[left]
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[left] >= nums[mid]:
                right = mid
            else:
                left = mid
        return min(nums[left], nums[right])
