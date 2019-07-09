_author_ = 'jake'
_project_ = 'leetcode'







class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        return " ".join(words[::-1])
