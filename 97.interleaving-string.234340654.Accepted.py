class Solution:
    def isInterleave(self, s1, s2, s3):













        m, n = len(s1), len(s2)
        if len(s3) != m + n:
            return False
        dp = [False] * (m + 1)
        dp[0] = True
        for i in range(1, m + 1):
            dp[i] = dp[i - 1] and s1[i - 1] == s3[i - 1]
        for j in range(1, n + 1):
            dp[0] = dp[0] and s2[j - 1] == s3[j - 1]
            for i in range(1, m + 1):
                dp[i] = (dp[i] and s3[i + j - 1] == s2[j - 1]) or (dp[i - 1] and s3[i + j - 1] == s1[i - 1])
        return dp[m]
