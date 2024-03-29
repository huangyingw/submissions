class Solution(object):
    def maxKilledEnemies(self, grid):

        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        max_kill_enemies, row_kill, col_kill = 0, 0, [0 for _ in range(cols)]
        for r in range(rows):
            for c in range(cols):
                if c == 0 or grid[r][c - 1] == "W":
                    row_kill, i = 0, c
                    while i < cols and grid[r][i] != "W":
                        row_kill += grid[r][i] == "E"
                        i += 1
                if r == 0 or grid[r - 1][c] == "W":
                    col_kill[c], i = 0, r
                    while i < rows and grid[i][c] != "W":
                        col_kill[c] += grid[i][c] == "E"
                        i += 1
                if grid[r][c] == "0":
                    max_kill_enemies = max(max_kill_enemies, row_kill + col_kill[c])
        return max_kill_enemies
