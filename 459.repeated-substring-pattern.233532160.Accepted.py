_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in (s[1:] + s[:-1])
