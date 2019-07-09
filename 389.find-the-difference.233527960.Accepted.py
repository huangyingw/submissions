_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counts = [0 for _ in range(26)]
        for c in s:
            counts[ord(c) - ord("a")] += 1
        for c in t:
            index = ord(c) - ord("a")
            counts[index] -= 1
            if counts[index] < 0:
                return c
