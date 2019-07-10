_author_ = 'jake'
_project_ = 'leetcode'








from collections import Counter


class Solution(object):
    def minWindow(self, s, t):

        freq = Counter(t)
        best_start, best_end = 0, float('inf')
        start, end = 0, -1
        to_match = len(t)
        while end < len(s) - 1 or to_match == 0:
            if to_match != 0:
                end += 1
                if s[end] in freq:
                    freq[s[end]] -= 1
                    if freq[s[end]] >= 0:
                        to_match -= 1
            else:
                if end - start < best_end - best_start:
                    best_end = end
                    best_start = start
                if s[start] in freq:
                    freq[s[start]] += 1
                    if freq[s[start]] > 0:
                        to_match += 1
                start += 1
        if best_end == float('inf'):
            return ''
        return s[best_start:best_end + 1]
