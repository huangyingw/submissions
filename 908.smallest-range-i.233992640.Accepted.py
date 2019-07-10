_author_ = 'jake'
_project_ = 'leetcode'










class Solution:
    def smallestRangeI(self, A, K):

        range = max(A) - min(A)
        return max(0, range - 2 * K)
