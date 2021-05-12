class Solution:
    def islandPerimeter(self, grid):
        l = n = 0
        a = len(grid)
        b = len(grid[0])
        for i in range(a):
            for j in range(b):
                if grid[i][j] == 1:
                    n += 1
                    if i < a - 1 and j < b - 1:
                        l = l + grid[i][j + 1] + grid[i + 1][j]
                    elif i < a - 1:
                        l += grid[i + 1][j]
                    elif j < b - 1:
                        l += grid[i][j + 1]
        s = 4 * n - 2 * l
        return s
