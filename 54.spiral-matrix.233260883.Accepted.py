_author_ = 'jake'
_project_ = 'leetcode'







class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        spiral = []
        row, col = 0, -1
        d_row, d_col = 0, 1
        row_leg, col_leg = len(matrix[0]), len(matrix) - 1
        leg_count = 0
        for _ in range(len(matrix[0]) * len(matrix)):
            row += d_row
            col += d_col
            spiral.append(matrix[row][col])
            leg_count += 1

            if (d_col != 0 and leg_count == row_leg) or (d_row != 0 and leg_count == col_leg):
                if d_col != 0:
                    row_leg -= 1
                else:
                    col_leg -= 1
                d_row, d_col = d_col, -d_row
                leg_count = 0
        return spiral
