_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1
        end = -1
        while i >= 0:
            if s[i] == ' ' and end != -1:
                return end - i
            if s[i] != ' ' and end == -1:
                end = i
            i -= 1
        return end + 1 if end != -1 else 0
