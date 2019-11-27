class Solution(object):
    def climbStairs(self, n):
        if n == 0:
            return 0
        dp = [0] * n
        dp[0], dp[1] = 1, 2
        for index in range(2, n):
            dp[index] = dp[index - 1] + dp[index - 2]
        return dp[n - 1]
