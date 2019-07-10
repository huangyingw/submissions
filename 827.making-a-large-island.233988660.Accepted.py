







from collections import defaultdict


class Solution(object):
    def largestIsland(self, grid):

        rows, cols = len(grid), len(grid[0])
        nbors = ((0, 1), (1, 0), (-1, 0), (0, -1))

        def island(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if grid[r][c] == 2:
                return 0
            if grid[r][c] == 0:
                edge.add((r, c))
                return 0
            grid[r][c] = 2
            return 1 + sum(island(r + dr, c + dc) for dr, dc in nbors)
        cell_to_areas = defaultdict(int)
        for r in range(rows):
            for c in range(cols):
                edge = set()
                area = island(r, c)
                if area != 0:
                    for cell in edge:
                        cell_to_areas[cell] += area
        if not cell_to_areas:
            return 1 if grid[0][0] == 0 else rows * cols
        return 1 + max(areas for areas in cell_to_areas.values())
