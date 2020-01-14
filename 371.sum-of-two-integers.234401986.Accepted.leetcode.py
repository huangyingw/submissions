class Solution:
    def getSum(self, a, b):
        tmp = [a, b]
        return sum(tmp)
    def getSum(self, a, b):
        MOD = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        while b != 0:
            a, b = (a ^ b) & MOD, ((a & b) << 1) & MOD
        return a if a <= MAX_INT else ~(a & MAX_INT) ^ MAX_INT
