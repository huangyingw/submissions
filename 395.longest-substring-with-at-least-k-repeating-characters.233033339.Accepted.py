


class Solution(object):
    def longestSubstring(self, s, k):
        dict = {}
        for c in s:
            if c not in dict:
                dict[c] = 0
            dict[c] += 1
        if all(dict[i] >= k for i in dict):
            return len(s)
        longest = 0
        start = 0
        for i in range(len(s)):
            c = s[i]
            if dict[c] < k:
                longest = max(longest, self.longestSubstring(s[start:i], k))
                start = i + 1
        return max(longest, self.longestSubstring(s[start:], k))
