class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    self.set_island(r, c, grid)
        return islands
    def set_island(self, row, col, grid):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return
        if grid[row][col] != '1':
            return
        grid[row][col] = '0'
        self.set_island(row + 1, col, grid)
        self.set_island(row - 1, col, grid)
        self.set_island(row, col + 1, grid)
        self.set_island(row, col - 1, grid)
