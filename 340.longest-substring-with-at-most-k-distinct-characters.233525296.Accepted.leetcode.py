from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        start, longest = 0, 0
        last_seen = defaultdict(int)
        for end, c in enumerate(s):
            last_seen[c] = end
            while len(last_seen) > k:
                if last_seen[s[start]] == start:
                    del last_seen[s[start]]
                start += 1
            else:
                longest = max(longest, end - start + 1)
        return longest
