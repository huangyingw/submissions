_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        a, b = len(str1), len(str2)
        if a < b:
            a, b = b, a
        while b != 0:
            a, b = b, a % b
        candidate = str1[:a]
        return candidate if str1 == candidate * (len(str1) // a) and str2 == candidate * (len(str2) // a) else ""
