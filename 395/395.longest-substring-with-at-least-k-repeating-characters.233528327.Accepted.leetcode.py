from collections import Counter


class Solution(object):
    def longestSubstring(self, s, k):
        longest = 0
        to_split = [s]
        while to_split:
            t = to_split.pop()
            freq = Counter(t)
            splitted = [t]
            for c in freq:
                if freq[c] < k:
                    new_splitted = []
                    for spl in splitted:
                        new_splitted += spl.split(c)
                    splitted = new_splitted
            if len(splitted) == 1:
                longest = max(longest, len(splitted[0]))
            else:
                to_split += [spl for spl in splitted if len(spl) > longest]
        return longest
