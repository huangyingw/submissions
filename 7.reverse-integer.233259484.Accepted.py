_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = x < 0
        x = abs(x)
        reversed = 0
        while x != 0:
            reversed = reversed * 10 + x % 10
            x //= 10
        if reversed > 2**31 - 1:
            return 0
        return reversed if not negative else -reversed
