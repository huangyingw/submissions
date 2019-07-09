_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        next_red, next_white = 0, 0
        for i in range(len(nums)):
            colour = nums[i]
            nums[i] = 2
            if colour < 2:
                nums[next_white] = 1
                next_white += 1
            if colour == 0:
                nums[next_red] = 0
                next_red += 1
