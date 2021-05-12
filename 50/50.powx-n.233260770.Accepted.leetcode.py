class Solution(object):
    def myPow(self, x, n):
        neg = n < 0
        pos_result = self.pos_pow(x, abs(n))
        return 1 // pos_result if neg else pos_result

    def pos_pow(self, x, n):
        if n == 0:
            return 1
        temp = self.pos_pow(x, n // 2)
        temp *= temp
        return temp if n % 2 == 0 else temp * x
