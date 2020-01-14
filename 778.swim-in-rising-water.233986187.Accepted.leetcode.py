import heapq
class Solution(object):
    def swimInWater(self, grid):
        N = len(grid)
        shifts = ((0, 1), (0, -1), (1, 0), (-1, 0))
        frontier = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        max_water = 0
        while True:
            water, r, c = heapq.heappop(frontier)
            max_water = max(max_water, water)
            if r == c == N - 1:
                return max_water
            for dr, dc in shifts:
                if r + dr < 0 or r + dr >= N or c + dc < 0 or c + dc >= N:
                    continue
                if (r + dr, c + dc) in visited:
                    continue
                visited.add((r + dr, c + dc))
                heapq.heappush(frontier, (grid[r + dr][c + dc], r + dr, c + dc))
