class Solution:
    def isHappy(self, n):
        while n > 1:
            nextN = 0
            while n:
                nextN += (n % 10) * (n % 10)
                n //= 10
            n = nextN
        return n == 1
