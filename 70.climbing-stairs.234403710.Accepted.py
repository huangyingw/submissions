
class Solution:

    def climbStairs(self, n):

        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b = 1, 2
        for i in range(3, n + 1):
            temp = a + b
            a, b = b, temp
        return temp
