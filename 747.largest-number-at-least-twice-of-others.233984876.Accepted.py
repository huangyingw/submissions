_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def dominantIndex(self, nums):

        first_i = 0
        second = 0
        for i, num in enumerate(nums[1:], 1):
            if num >= nums[first_i]:
                first_i, second = i, nums[first_i]
            elif num > second:
                second = num
        return first_i if nums[first_i] >= 2 * second else -1
