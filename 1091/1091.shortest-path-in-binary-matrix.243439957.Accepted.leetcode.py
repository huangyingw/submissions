class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        front, back = {(0, 0)}, {(n - 1, n - 1)}
        visited = set()
        path = 0
        while front and back:
            path += 1
            if front & back:
                return path
            if len(front) > len(back):
                front, back = back, front
            new_front = set()
            for r, c in front:
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if r + dr < 0 or r + dr >= n:
                            continue
                        if c + dc < 0 or c + dc >= n:
                            continue
                        if grid[r + dr][c + dc] == 1:
                            continue
                        new_front.add((r + dr, c + dc))
            visited |= front
            new_front -= visited
            front = new_front
        return -1
