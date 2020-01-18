class Solution:
    def minPathSum(self, grid):
        if not grid or len(grid) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        curr = [0] * m
        curr[0] = grid[0][0]
        for i in range(1, m):
            curr[i] = curr[i - 1] + grid[i][0]
        for j in range(1, n):
            curr[0] += grid[0][j]
            for i in range(1, m):
                curr[i] = min(curr[i - 1], curr[i]) + grid[i][j]
        return curr[m - 1]
