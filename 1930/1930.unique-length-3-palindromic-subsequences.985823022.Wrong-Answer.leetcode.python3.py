class Solution:
    def countPalindromicSubsequence(self, s):

        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
        count = 0
        for i in range(n):
            for j in range(i + 2, n):
                count += dp[i][j]
        return count
