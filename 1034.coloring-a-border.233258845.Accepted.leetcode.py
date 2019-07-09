_author_ = 'jake'
_project_ = 'leetcode'



















class Solution(object):
    def colorBorder(self, grid, r0, c0, color):
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        original = grid[r0][c0]
        rows, cols = len(grid), len(grid[0])
        connected = set()

        def dfs(r, c):
            if (r, c) in connected:
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != original:
                return False
            connected.add((r, c))
            if not sum(dfs(r + dr, c + dc) for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]) == 4:
                grid[r][c] = color
            return True
        dfs(r0, c0)
        return grid
