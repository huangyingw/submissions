class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        start, max_substring = 0, 0
        last_seen = {}
        for i, c in enumerate(s):
            if c in last_seen or len(last_seen) < 2:
                max_substring = max(max_substring, i - start + 1)
            last_seen[c] = i
        return max_substring
