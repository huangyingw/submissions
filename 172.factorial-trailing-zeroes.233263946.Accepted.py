_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def trailingZeroes(self, n):

        zeroes = 0
        power_of_5 = 5
        while power_of_5 <= n:
            zeroes += n // power_of_5
            power_of_5 *= 5
        return zeroes
