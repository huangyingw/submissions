class Solution(object):
    def shortestPathAllKeys(self, grid):
        rows, cols = len(grid), len(grid[0])
        possible_keys = set("abcdef")
        keys = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "@":
                    start_r, start_c = r, c
                elif grid[r][c] in possible_keys:
                    keys.add(grid[r][c])
        steps = 0
        frontier = [(start_r, start_c, "")]
        visited = set()
        neighbours = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while frontier:
            new_frontier = set()
            for r, c, open_locks in frontier:
                if (r, c, open_locks) in visited:
                    continue
                if r < 0 or r >= rows or c < 0 or c >= cols:
                    continue
                if grid[r][c] == "
                continue
                if "A" <= grid[r][c] <= "F" and grid[r][c] not in open_locks:
                    continue
                visited.add((r, c, open_locks))
                if grid[r][c] in keys and grid[r][c].upper() not in open_locks:
                    open_locks = "".join(sorted(open_locks + grid[r][c].upper()))
                if len(open_locks) == len(keys):
                    return steps
                for dr, dc in neighbours:
                    new_frontier.add((r + dr, c + dc, open_locks))
            frontier = new_frontier
            steps += 1
        return -1
