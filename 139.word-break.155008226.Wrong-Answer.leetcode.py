



















































class Solution(object):
    def wordBreak(self, s, wordDict):

        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for start in range(len(s)):
            if not dp[start]:
                continue
            for end in range(start + 1, len(s)):
                if s[start:end] in wordDict:
                    dp[end] = True
        return dp[len(s)]
