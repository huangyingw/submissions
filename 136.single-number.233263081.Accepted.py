_author_ = 'jake'
_project_ = 'leetcode'







class Solution(object):
    def singleNumber(self, nums):

        xor = 0
        for num in nums:
            xor ^= num
        return xor
