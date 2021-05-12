class Solution(object):
    def dieSimulator(self, n, rollMax):
        sides = len(rollMax)
        dp = [[0 for j in range(sides)] for i in range(n + 1)]
        dp_total = [0] * (n + 1)
        dp_total[0], dp_total[1] = 1, 6
        for j in range(sides):
            dp[1][j] = 1
        for i in range(2, n + 1):
            for j in range(sides):
                for k in range(1, rollMax[j] + 1):
                    if i - k < 0:
                        break
                    dp[i][j] += dp_total[i - k] - dp[i - k][j]
            dp_total[i] = sum(dp[i])
        return dp_total[n] % (10 ** 9 + 7)
