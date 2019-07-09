_author_ = 'jake'
_project_ = 'leetcode'







class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for c in s:
            result = result * 26 + ord(c) - ord('A') + 1
        return result
