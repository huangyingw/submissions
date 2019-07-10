













class Solution(object):
    def numDistinctIslands2(self, grid):

        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])

        def BFS(base_r, base_c):
            grid[base_r][base_c] = 0
            queue = [(base_r, base_c)]
            for r, c in queue:
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_r, new_c = r + dr, c + dc
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 0
                        queue.append((new_r, new_c))
            canonical = []
            for _ in range(4):
                queue = [(c, -r) for r, c in queue]
                min_r, min_c = min([r for r, _ in queue]), min([c for _, c in queue])
                canonical = max(canonical, sorted([(r - min_r, c - min_c) for r, c in queue]))
                reflected = [(r, -c) for r, c in queue]
                min_r, min_c = min([r for r, _ in reflected]), min([c for _, c in reflected])
                canonical = max(canonical, sorted([(r - min_r, c - min_c) for r, c in reflected]))
            return tuple(canonical)
        islands = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                islands.add(BFS(r, c))
        return len(islands)
