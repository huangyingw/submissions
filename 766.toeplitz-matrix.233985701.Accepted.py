








class Solution(object):
    def isToeplitzMatrix(self, matrix):

        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows - 1):
            for c in range(cols - 1):
                if matrix[r][c] != matrix[r + 1][c + 1]:
                    return False
        return True
