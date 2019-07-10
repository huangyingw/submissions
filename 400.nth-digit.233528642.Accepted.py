_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def findNthDigit(self, n):

        length = 1
        digits = 9
        while n > digits:
            n -= digits
            digits = (length + 1) * 9 * (10 ** length)
            length += 1
        start = 10 ** (length - 1)
        num, digit = divmod(n - 1, length)
        num += start
        return int(str(num)[digit])
