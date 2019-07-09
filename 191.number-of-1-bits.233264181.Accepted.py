_author_ = 'jake'
_project_ = 'leetcode'







class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum(c == "1" for c in bin(n)[2:])
