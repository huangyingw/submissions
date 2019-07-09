
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """







        base = 5
        ans = 0
        while base <= n:
            ans += n // base
            base *= 5
        return ans
