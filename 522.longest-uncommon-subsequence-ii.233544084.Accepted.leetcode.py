from collections import Counter
class Solution(object):
    def findLUSlength(self, strs):
        def is_subsequence(s, t):
            i, j = 0, 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                j += 1
            if i == len(s):
                return True
            return False
        counts = Counter(strs)
        unique_strs = list(counts.keys())
        unique_strs.sort(key=len, reverse=True)
        seen = set()
        for s in unique_strs:
            if counts[s] == 1:
                if not any([is_subsequence(s, t) for t in seen]):
                    return len(s)
            else:
                seen.add(s)
        return -1
