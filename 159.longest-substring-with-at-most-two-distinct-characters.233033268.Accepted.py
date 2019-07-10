class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, j, maxLen = 0, -1, 0
        for k in range(1, len(s)):
            if s[k] == s[k - 1]:
                continue
            if j >= 0 and s[j] != s[k]:
                maxLen = max(k - i, maxLen)
                i = j + 1
            j = k - 1
        return max(len(s) - i, maxLen)
