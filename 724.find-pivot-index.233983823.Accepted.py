_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def pivotIndex(self, nums):

        left, right = 0, sum(nums)
        for i, num in enumerate(nums):
            right -= num
            if left == right:
                return i
            left += num
        return -1
