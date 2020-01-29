class Solution:
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        while n > 1:
            if n % 3 == 0:
                n /= 3
            else:
                return False
        return True

    def isPowerOfThree(self, n):
        return n > 0 and 1162261467 % n == 0

    def isPowerOfThree(self, n):
        return n > 0 and (n == 1 or (n % 3 == 0 and self.isPowerOfThree(n / 3)))
