import heapq


class Solution(object):
    def shortestPath(self, grid, k):
        rows, cols = len(grid), len(grid[0])

        def heuristic(r, c):
            return abs(rows - 1 - r) + abs(cols - 1 - c)
        queue = [(heuristic(0, 0), -k + grid[0][0], 0, 0, 0)]
        visited = {}
        while queue:
            _, neg_elims, steps, r, c = heapq.heappop(queue)
            if neg_elims > 0:
                continue
            if r == rows - 1 and c == cols - 1:
                return steps
            if (r, c) in visited and neg_elims >= visited[(r, c)]:
                continue
            visited[(r, c)] = neg_elims
            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                r2, c2 = r + dr, c + dc
                if r2 < 0 or r2 >= rows or c2 < 0 or c2 >= cols:
                    continue
                heapq.heappush(queue, (heuristic(r2, c2) + steps + 1, neg_elims + grid[r2][c2], steps + 1, r2, c2))
        return -1
