


class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        a, b = 1, 2
        for _ in range(2, n):
            a, b = b, a + b
        return b
