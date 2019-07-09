_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        return A in B + B
