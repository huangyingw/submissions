










class NumMatrix(object):
    def __init__(self, matrix):

        if not matrix or not matrix[0]:
            return
        rows, self.cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(1, self.cols):
                matrix[r][c] += matrix[r][c - 1]
        self.matrix = matrix

    def update(self, row, col, val):

        prev = self.matrix[row][col]
        if col != 0:
            prev -= self.matrix[row][col - 1]
        diff = val - prev
        for c in range(col, self.cols):
            self.matrix[row][c] += diff

    def sumRegion(self, row1, col1, row2, col2):

        sum_region = 0
        for r in range(row1, row2 + 1):
            sum_region += self.matrix[r][col2]
            if col1 != 0:
                sum_region -= self.matrix[r][col1 - 1]
        return sum_region
