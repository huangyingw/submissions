_author_ = 'jake'
_project_ = 'leetcode'








class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        while b != 0:
            total = (a ^ b) & MASK
            carry = ((a & b) << 1) & MASK
            a, b = total, carry
        return a if a < MAX_INT else ~(a ^ MASK)
