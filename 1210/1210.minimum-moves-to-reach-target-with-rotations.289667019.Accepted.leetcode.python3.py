class Solution(object):
    def minimumMoves(self, grid):
        rows, cols = len(grid), len(grid[0])
        moves = 0
        seen = set()
        frontier = {(0, 1, True)}
        while frontier:
            if (rows - 1, cols - 1, True) in frontier:
                return moves
            new_frontier = set()
            for r, c, horizontal in frontier:
                if (r, c, horizontal) in seen:
                    continue
                if horizontal and c != cols - 1 and grid[r][c + 1] == 0:
                    new_frontier.add((r, c + 1, True))
                if not horizontal and r != rows - 1 and grid[r + 1][c] == 0:
                    new_frontier.add((r + 1, c, False))
                if horizontal and r != rows - 1 and grid[r + 1][c] == 0 and grid[r + 1][c - 1] == 0:
                    new_frontier.add((r + 1, c, True))
                    new_frontier.add((r + 1, c - 1, False))
                if not horizontal and c != cols - 1 and grid[r][c + 1] == 0 and grid[r - 1][c + 1] == 0:
                    new_frontier.add((r, c + 1, False))
                    new_frontier.add((r - 1, c + 1, True))
            seen |= frontier
            frontier = new_frontier
            moves += 1
        return -1
