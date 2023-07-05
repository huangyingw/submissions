class Solution(object):
    def checkInclusion(self, s1, s2):
        n1 = len(s1)
        freq = {}
        for c in s1:
            freq[c] = freq.setdefault(c, 0) + 1
        for i, c in enumerate(s2):
            freq[c] = freq.setdefault(c, 0) - 1
            if i >= n1:
                freq[s2[i - n1]] = freq.setdefault(s2[i - n1], 0) + 1
            if all(value == 0 for value in freq.values()):
                return True
        return False
