_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        for num in range(N, 0, -1):
            if bin(num)[2:] not in S:
                return False
        return True
