_author_ = 'jake'
_project_ = 'leetcode'








class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not n & (n - 1)
