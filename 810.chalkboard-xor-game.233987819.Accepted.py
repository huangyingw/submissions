_author_ = 'jake'
_project_ = 'leetcode'












from functools import reduce
import operator


class Solution(object):
    def xorGame(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return reduce(operator.xor, nums) == 0 or len(nums) % 2 == 0
