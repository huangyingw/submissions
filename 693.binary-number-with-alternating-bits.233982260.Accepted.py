class Solution(object):
    def hasAlternatingBits(self, n):
        n, bit = divmod(n, 2)
        while n:
            if n % 2 == bit:
                return False
            n, bit = divmod(n, 2)
        return True
