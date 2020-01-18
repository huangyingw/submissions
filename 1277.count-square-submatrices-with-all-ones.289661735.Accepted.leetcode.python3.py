class Solution(object):
    def countSquares(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        for r in range(1, rows):
            for c in range(1, cols):
                matrix[r][c] *= 1 + min(matrix[r - 1][c], matrix[r][c - 1], matrix[r - 1][c - 1])
        return sum(map(sum, matrix))
