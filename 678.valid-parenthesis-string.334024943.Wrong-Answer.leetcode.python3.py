class Solution(object):
    def checkValidString(self, s):
        L = ['(', '*']
        R = [')', '*']
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i] == '*':
                    dp[i][i] = True
                if i + 1 < len(s) and j - 1 >= 0 and dp[i + 1][j - 1] and s[i] in L and s[j] in R:
                    dp[i][j] = True
                for k in range(i, j):
                    if dp[i][k] and dp[k + 1][j]:
                        dp[i][j] = True
                        break
        return dp[0][len(s) - 1]
