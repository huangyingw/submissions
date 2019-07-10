






class Solution(object):
    def firstUniqChar(self, s):

        counts = [0 for _ in range(26)]
        for c in s:
            counts[ord(c) - ord("a")] += 1
        for i, c in enumerate(s):
            if counts[ord(c) - ord("a")] == 1:
                return i
        return -1
