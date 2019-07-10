_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def arrayPairSum(self, nums):

        return sum(sorted(nums)[::2])
