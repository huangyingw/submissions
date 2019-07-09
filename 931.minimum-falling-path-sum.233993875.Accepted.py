_author_ = 'jake'
_project_ = 'leetcode'










class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        n = len(A)
        row_minima = [0] * n
        for r in range(n - 1, -1, -1):
            new_row_minima = list(A[r])
            for c in range(n):
                new_row_minima[c] += min(row_minima[max(0, c - 1):c + 2])
            row_minima = new_row_minima
        return min(row_minima)
