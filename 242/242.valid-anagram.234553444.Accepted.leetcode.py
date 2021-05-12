import collections


class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        letters = collections.defaultdict(int)
        for c in s:
            letters[c] += 1
        for c in t:
            if letters[c] <= 0:
                return False
            letters[c] -= 1
        return True
