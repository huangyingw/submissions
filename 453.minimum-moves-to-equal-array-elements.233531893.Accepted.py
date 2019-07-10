_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def minMoves(self, nums):

        return sum(nums) - min(nums) * len(nums)
