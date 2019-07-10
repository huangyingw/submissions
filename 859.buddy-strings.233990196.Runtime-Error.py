class Solution(object):
    def matrixScore(self, A):
        rows, cols = len(A), len(A[0])
        for r in range(rows):
            if A[r][0] == 0:
                for c in range(1, cols):
                    A[r][c] = 1 - A[r][c]
        score = rows * 2 ** (cols - 1)
        for c in range(1, cols):
            col_count = sum(A[r][c] for r in range(rows))
            best_col_count = max(col_count, rows - col_count)
            col_val = 2 ** ((cols - 1) - c)
            score += col_val * best_col_count
        return score
