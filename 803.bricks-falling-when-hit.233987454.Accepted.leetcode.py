class Solution(object):
    def hitBricks(self, grid, hits):
        rows, cols = len(grid), len(grid[0])
        nbors = ((1, 0), (0, 1), (-1, 0), (0, -1))
        for r, c in hits:
            grid[r][c] -= 1

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0
            if grid[row][col] != 1:
                return 0
            grid[row][col] = 2
            return 1 + sum(dfs(row + dr, col + dc) for dr, dc in nbors)
        for c in range(cols):
            dfs(0, c)

        def connected(r, c):
            if r == 0:
                return True
            return any(0 <= (r + dr) < rows and 0 <= (c + dc) < cols \
                       and grid[r + dr][c + dc] == 2 for dr, dc in nbors)
        result = []
        for r, c in reversed(hits):
            grid[r][c] += 1
            if grid[r][c] == 1 and connected(r, c):
                result.append(dfs(r, c) - 1)
            else:
                result.append(0)
        return result[::-1]
