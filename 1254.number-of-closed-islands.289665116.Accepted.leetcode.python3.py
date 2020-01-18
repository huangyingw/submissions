class Solution(object):
    def closedIsland(self, grid):
        rows, cols = len(grid), len(grid[0])
        nbors = [[1, 0], [0, 1], [-1, 0], [0, - 1]]

        def closed(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return True
            if grid[r][c] == 1:
                return True
            is_closed = 0 < r < rows - 1 and 0 < c < cols - 1
            grid[r][c] = 1
            for dr, dc in nbors:
                is_closed = closed(r + dr, c + dc) and is_closed
            return is_closed
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    islands += int(closed(r, c))
        return islands
