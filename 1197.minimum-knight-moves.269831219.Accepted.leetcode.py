import heapq
class Solution(object):
    def minKnightMoves(self, x, y):
        def heuristic(cell):
            dx, dy = abs(cell[0] - x), abs(cell[1] - y)
            min_d, max_d = sorted([dx, dy])
            max_moves = (max_d + 1) // 2
            return max_moves + max(0, (min_d - max_moves + 1) // 2)
        queue = [[heuristic((0, 0)), 0, (0, 0)]]
        seen = set()
        while True:
            _, moves, cell = heapq.heappop(queue)
            if cell == (x, y):
                return moves
            if cell in seen:
                continue
            seen.add(cell)
            for dx, dy in [(2, 1), (2, -1), (-2, -1), (-2, 1), (1, 2), (-1, 2), (-1, -2), (1, -2)]:
                new_cell = (cell[0] + dx, cell[1] + dy)
                if new_cell not in seen:
                    heapq.heappush(queue, [heuristic(new_cell) + moves + 1, moves + 1, new_cell])
