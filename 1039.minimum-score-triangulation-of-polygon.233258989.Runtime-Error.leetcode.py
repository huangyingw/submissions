_author_ = 'jake'
_project_ = 'leetcode'











from functools import lru_cache


class Solution(object):
    def minScoreTriangulation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        @lru_cache(None)
        def helper(i, j):
            if j - i <= 1:
                return 0
            return min(helper(i, k) + A[i] * A[k] * A[j] + helper(k, j) for k in range(i + 1, j))
        return helper(0, len(A) - 1)
