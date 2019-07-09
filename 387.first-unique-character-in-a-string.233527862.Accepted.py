_author_ = 'jake'
_project_ = 'leetcode'







class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = [0 for _ in range(26)]
        for c in s:
            counts[ord(c) - ord("a")] += 1
        for i, c in enumerate(s):
            if counts[ord(c) - ord("a")] == 1:
                return i
        return -1
