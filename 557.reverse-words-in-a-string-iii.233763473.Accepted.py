_author_ = 'jake'
_project_ = 'leetcode'








class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join([w[::-1] for w in s.split(" ")])
