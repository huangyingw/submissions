class Solution(object):
    def cherryPickup(self, grid):
        n = len(grid)
        memo = {}
        def helper(r1, c1, r2):
            c2 = r1 + c1 - r2
            if r1 == n or c1 == n or r2 == n or c2 == n:
                return float("-inf")
            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float("-inf")
            if r1 == n - 1 and c1 == n - 1:
                return grid[n - 1][n - 1]
            if (r1, c1, r2) in memo:
                return memo[(r1, c1, r2)]
            result = grid[r1][c1]
            if r2 != r1 or c2 != c1:
                result += grid[r2][c2]
            result += max(helper(r1 + 1, c1, r2 + 1), helper(r1, c1 + 1, r2),
                          helper(r1 + 1, c1, r2), helper(r1, c1 + 1, r2 + 1))
            memo[(r1, c1, r2)] = result
            return result
        return max(0, helper(0, 0, 0))
