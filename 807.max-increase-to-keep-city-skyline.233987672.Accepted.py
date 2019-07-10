













class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):

        rows, cols = len(grid), len(grid[0])
        row_sky = [0 for _ in range(rows)]
        col_sky = [0 for _ in range(cols)]
        for r in range(rows):
            for c in range(cols):
                row_sky[r] = max(row_sky[r], grid[r][c])
                col_sky[c] = max(col_sky[c], grid[r][c])
        increase = 0
        for r in range(rows):
            for c in range(cols):
                increase += min(row_sky[r], col_sky[c]) - grid[r][c]
        return increase
