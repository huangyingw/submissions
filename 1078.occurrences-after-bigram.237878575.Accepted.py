_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def findOcurrences(self, text, first, second):

        result = []
        s = text.split()
        for i in range(2, len(s)):
            if s[i - 2] == first and s[i - 1] == second:
                result.append(s[i])
        return result
