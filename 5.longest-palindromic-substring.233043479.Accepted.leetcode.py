class Solution(object):
    def longestPalindrome(self, s):
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        maxLength, result = 1, ""
        for index in range(len(s)):
            dp[index][index] = 1
