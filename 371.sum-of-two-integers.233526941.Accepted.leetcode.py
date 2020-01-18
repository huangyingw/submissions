class Solution(object):
    def getSum(self, a, b):
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        while b != 0:
            total = (a ^ b) & MASK
            carry = ((a & b) << 1) & MASK
            a, b = total, carry
        return a if a < MAX_INT else ~(a ^ MASK)
