_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def search(self, nums, target):

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1
