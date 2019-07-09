_author_ = 'jake'
_project_ = 'leetcode'










class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        range = max(A) - min(A)
        return max(0, range - 2 * K)
