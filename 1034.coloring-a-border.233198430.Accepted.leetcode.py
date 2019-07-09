


class Solution(object):
    def colorBorder(self, grid, r0, c0, color):
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        if not grid:
            return grid
        visited, border = [], []
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] != grid[r0][c0] or (r, c) in visited:
                return
            visited.append((r, c))
            # check if the current row, col index is edge of the matrix
            # if not then check adjacent cells doesnt have same value as grid[r0][c0] then add in border
            if (r == 0 or c == 0 or r == m - 1 or c == n - 1 or
                (r + 1 < m and grid[r + 1][c] != grid[r0][c0]) or
                (r - 1 >= 0 and grid[r - 1][c] != grid[r0][c0]) or
                (c + 1 < n and grid[r][c + 1] != grid[r0][c0]) or
                (c - 1 >= 0 and grid[r][c - 1] != grid[r0][c0])):
                border.append((r, c))
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        dfs(r0, c0)
        for (x, y) in border:
            grid[x][y] = color
        return grid
