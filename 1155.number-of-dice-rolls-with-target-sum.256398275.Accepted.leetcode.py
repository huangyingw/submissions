class Solution(object):
    def numRollsToTarget(self, d, f, target):
        MOD = 10 ** 9 + 7
        dp = [[0 for _ in range(target + 1)] for _ in range(d + 1)]
        dp[0][0] = 1
        for die in range(1, d + 1):
            for total in range(die, target + 1):
                dp[die][total] = sum(dp[die - 1][max(total - f, 0):total]) % MOD
        return dp[-1][-1]
