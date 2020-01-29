class Solution(object):
    def singleNonDuplicate(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1:
                mid -= 1
            if mid + 1 == len(nums) or nums[mid + 1] != nums[mid]:
                right = mid
            else:
                left = mid + 2
        return nums[left]
