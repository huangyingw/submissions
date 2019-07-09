_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        for row in grid:
            row.append(0)
        grid.append([0] * (cols + 1))
        perimiter = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimiter += 4
                    if grid[r + 1][c] == 1:
                        perimiter -= 2
                    if grid[r][c + 1] == 1:
                        perimiter -= 2
        return perimiter
