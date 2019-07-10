

















class Solution(object):
    def minDeletionSize(self, A):

        rows, cols = len(A), len(A[0])
        max_subsequence = [1] * cols
        for col_end in range(1, cols):
            for col in range(col_end):
                if all(A[r][col] <= A[r][col_end] for r in range(rows)):
                    max_subsequence[col_end] = max(max_subsequence[col_end],
                                                   max_subsequence[col] + 1)
        return cols - max(max_subsequence)
