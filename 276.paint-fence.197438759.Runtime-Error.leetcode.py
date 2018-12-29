class Solution(object):
    def numWays(self, n, k):
        if n == 1:
            return k

        if n == 2:
            return k * (k - 1)

        dp = [0] * n

        for idx in range(2, n):
            dp[idx] = (k - 1) * (dp[idx - 1] + dp[idx - 2])

        return dp[n - 1]
