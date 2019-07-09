_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        guess = x
        while guess * guess > x:
            guess = (guess + x // guess) // 2
        return guess
