class Solution(object):
    def isValidPalindrome(self, s, k):
        memo = {}

        def helper(start, end):
            if start >= end:
                return 0
            if (start, end) in memo:
                return memo[(start, end)]
            if s[start] == s[end]:
                result = helper(start + 1, end - 1)
            else:
                result = 1 + min(helper(start + 1, end), helper(start, end - 1))
            memo[(start, end)] = result
            return result
        return helper(0, len(s) - 1) <= k
