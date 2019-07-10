









class Solution(object):
    def countCornerRectangles(self, grid):

        rows, cols = len(grid), len(grid[0])
        cols_by_row = []
        for r in range(rows):
            cols_by_row.append(set((c for c in range(cols) if grid[r][c])))
        rectangles = 0
        for high_row in range(1, rows):
            for low_row in range(high_row):
                common_cols = len(cols_by_row[high_row] & cols_by_row[low_row])
                if common_cols >= 2:
                    rectangles += common_cols * (common_cols - 1) // 2
        return rectangles
