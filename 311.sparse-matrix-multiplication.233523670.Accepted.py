class Solution(object):
    def multiply(self, A, B):
        rows_A, cols_A = len(A), len(A[0])
        cols_B = len(B[0])
        C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
        for r in range(rows_A):
            for c in range(cols_A):
                if A[r][c] != 0:
                    for i in range(cols_B):
                        C[r][i] += A[r][c] * B[c][i]
        return C
