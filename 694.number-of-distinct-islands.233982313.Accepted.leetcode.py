class Solution(object):
    def numDistinctIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])

        def BFS(r, c):
            queue = [(0, 0)]
            for r_rel, c_rel in queue:
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_r, new_c = r_rel + dr + r, c_rel + dc + c
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 0
                        queue.append((new_r - r, new_c - c))
            return tuple(queue)
        islands = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                islands.add(BFS(r, c))
        return len(islands)
