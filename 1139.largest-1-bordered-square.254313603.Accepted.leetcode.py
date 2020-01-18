class Solution(object):
    def largest1BorderedSquare(self, grid):
        rows, cols = len(grid), len(grid[0])
        best = 0
        for row in range(rows):
            sequence = 0
            for col in range(cols):
                if best >= rows - row:
                    return best * best
                if grid[row][col] == 1:
                    sequence += 1
                else:
                    sequence = 0
                if best >= sequence:
                    continue
                for side in range(min(sequence, rows - row), best, -1):
                    if not all(grid[r][col] and grid[r][col - side + 1] for r in range(row + 1, row + side)):
                        continue
                    if not all(grid[row + side - 1][col - side + 1:col + 1]):
                        continue
                    best = side
                    break
        return best * best
