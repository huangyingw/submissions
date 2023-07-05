class Solution(object):
    def checkInclusion(self, s1, s2):

        n1 = len(s1)
        freq = [0] * 26
        for c in s1:
            freq[ord(c) - ord("a")] += 1
        for i, c in enumerate(s2):
            freq[ord(c) - ord("a")] -= 1
            if i >= n1:
                freq[ord(s2[i - n1]) - ord("a")] += 1
            if not any(freq):
                return True
        return False
