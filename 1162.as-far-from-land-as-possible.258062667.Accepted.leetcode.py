class Solution(object):
    def maxDistance(self, grid):
        rows, cols = len(grid), len(grid[0])
        visited = 0
        frontier = {(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 1}
        visited += len(frontier)
        if not frontier or visited == rows * cols:
            return -1
        neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        distance = 0
        while visited < rows * cols:
            new_frontier = set()
            for r, c in frontier:
                for dr, dc in neighbours:
                    if r + dr < 0 or r + dr >= rows:
                        continue
                    if c + dc < 0 or c + dc >= cols:
                        continue
                    if grid[r + dr][c + dc] == 0:
                        visited += 1
                        grid[r + dr][c + dc] = 1
                        new_frontier.add((r + dr, c + dc))
            frontier = new_frontier
            distance += 1
        return distance
