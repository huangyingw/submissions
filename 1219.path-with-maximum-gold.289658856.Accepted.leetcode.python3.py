class Solution(object):
    def getMaximumGold(self, grid):
        rows, cols = len(grid), len(grid[0])
        neighbours = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        def helper(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if grid[r][c] == 0:
                return 0
            gold = best = grid[r][c]
            grid[r][c] = 0
            for dr, dc in neighbours:
                best = max(best, gold + helper(r + dr, c + dc))
            grid[r][c] = gold
            return best
        result = 0
        for r in range(rows):
            for c in range(cols):
                result = max(result, helper(r, c))
        return result
